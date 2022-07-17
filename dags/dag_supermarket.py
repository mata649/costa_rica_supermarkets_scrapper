import os
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.bash import BashOperator
from airflow import DAG
from docker.types import Mount
from airflow.utils.dates import days_ago

default_args = {
    'start_date': days_ago(1)
}

supermarkets = ['pequeno_mundo']
docker_url = 'unix://var/run/docker.sock'
MOUNT_DATA_DIRECTORY = os.getenv('MOUNT_DATA_DIRECTORY')

with DAG(
    'dag_supermarket',
    default_args=default_args,
    description='A simple tutorial DAG',
    schedule_interval='@daily',
        tags=['example'],) as dag:

    extract_list = []
    transform_list = []
    load_list = []
   
    for supermarket in supermarkets:
        extract_name = f'extract_{supermarket}'
        transform_name = f'transform_{supermarket}'
        load_name = f'load_{supermarket}'

        extract = DockerOperator(task_id=extract_name,
                                 image='supermarket_etl',
                                 command=f'python3 /opt/application/src/extract.py --supermarket {supermarket}',
                                 auto_remove=True,
                                 mounts=[Mount(
                                     source=MOUNT_DATA_DIRECTORY,
                                     target='/opt/application/data',
                                     type='bind'
                                 )],
                                 )

        transform = DockerOperator(task_id=transform_name,
                                   image='supermarket_etl',
                                   command='python3 /opt/application/src/transform.py --args "{{ti.xcom_pull(task_ids="' +
                                   extract_name+'")}}" ',
                                   auto_remove=True,
                                   mounts=[Mount(
                                       source=MOUNT_DATA_DIRECTORY,
                                       target='/opt/application/data',
                                       type='bind'
                                   )],
                                   )
        load = DockerOperator(task_id=load_name,
                              image='supermarket_etl',
                              command='python3 /opt/application/src/load.py --file_paths "{{ti.xcom_pull(task_ids="' +
                              transform_name+'")}}" ',
                              auto_remove=True,
                              mounts=[Mount(
                                  source=MOUNT_DATA_DIRECTORY,
                                  target='/opt/application/data',
                                  type='bind'
                              )],
                              docker_url=docker_url,
                              network_mode='costa_rica_supermarkets_scrapper_default',

                              )
     
        extract_list.append(extract)
        transform_list.append(transform)
        load_list.append(load)

    test = DummyOperator(
            task_id="check_database",
            # ui_color='#e8f7e4'
        )
for extract, transform, load in zip(extract_list, transform_list, load_list):
    extract >> transform >> load  >>test
