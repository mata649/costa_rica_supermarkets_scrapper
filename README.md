
# costa_rica_supermarkets_scrapper

Data pipeline using Scrapy, Pandas, SQLAlchemy, and Airflow to extract, transform, and load structured product information. The project runs fully containerized with Docker Compose and demonstrates how to automate data workflows with orchestration tools.

## Requirements

 - **Docker compose:** Compose is a tool for defining and running multi-container Docker applications. With Compose, you use a YAML file to configure your application’s services. You can read more about Docker Compose [here](https://docs.docker.com/compose/)


## Installing Project Dependencies
As I said before, Docker Compose is a requirement because the installation from all we will need is in the file docker-compose.yaml. So you don't need to be worried about installing any dependency or service; that is Docker's magic. 

The next step is to run the next command to set up all our services, but before you run the command, you need to change something important in the **.env** file. In the last line, you will see an environment variable called **MOUNT_DATA_DIRECTORY**. By default, the variable has the value **/home/data**, but you have to change it to the directory where you want to save the .csv used in each process of the ETL, and also note that in case one process fails, it can be stored to be used in the next run. Another important thing is that it has to be an absolute path, so if you have Windows has to be something like **"C:\data"**.

So once the **MOUNT_DATA_DIRECTORY** was changed, you can run the next command to set up all the services.

    docker-compose up -d


## Services Explanation
The next diagram is going to help us understand how all the services are in the Docker Compose file and how they are related. The first important thing is to know that we are going to have **two Postgres databases**, one is used as the **Airflow Metadatabase** and the other is used for the ETL to load the data. The airflow services are separated into different containers, one is used for the **webserver**, another for the **scheduler**, and the last is used to set up the configuration from the airflow service and creates the **metadatabase**. The **supermarket_etl_init** is a container used to run the **alembic** commands to run the migration and create the tables in the **postgres_etl database**. 


![Diagram](https://github.com/mata649/costa_rica_supermarkets_scrapper/blob/images/supermarket_etl.jpg?raw=true)


The last is the containers created by our **airflow scheduler**; those containers are created and auto-removed by **DockerOperator**.  The DockerOperator is used to run each process from our ETL, creating a Docker container for each process. When the load process is executed, this loads the information to the **Postgrest ETL Database**   

Finally, we have a **pgAdmin4** container, to see both databases, this container is preconfigured with the connection to our database through the file **servers.json**.
 ### Access to PgAdmin4
 - **URL:**  `locahost:5050`  
 -  **Email:** `admin@admin.com`
 -  **Password:** `root`

### Access to Airflow Webserver 
 - **URL:**  `locahost:8080`  
 -  **Username:** `airflow`
 -  **Password:** `airflow`

   
## ER Diagram

![enter image description here](https://github.com/mata649/costa_rica_supermarkets_scrapper/blob/images/ERD%20diagram.png?raw=true)

## Running ETL Process

The ETL process is configured to run daily. You can change this by modifying the **dag_supermarket.py** in the folder **dags**. Also, you can check the workflows by accessing the **airflow webserver**. If you have a problem running the ETL, please contact me or open an issue. Finally, I would like to remind you to change the **MOUNT_DATA_DIRECTORY** variable in the **.env**, as I explained before, this is important to run the ETL.
