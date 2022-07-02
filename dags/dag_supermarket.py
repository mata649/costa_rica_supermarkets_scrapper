from cgi import test
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago

default_args ={
    'start_date': days_ago(1)
}

with DAG(
    'dag_supermarket',
    default_args=default_args,
    description='A simple tutorial DAG',
    schedule_interval='@daily',
    tags=['example'],) as dag:
    test2 = BashOperator(
        task_id="test2",
        bash_command='',
        do_xcom_push=True      
    )
    