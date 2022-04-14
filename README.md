# costa_rica_supermarkets_scrapper

This ETL process extracts product information from the main supermarkets in Costa Rica and stores product price information over time. For this project I used **scrapy** to extract the information, **pandas** to transform and normalize the information and **SQLAlchemy** to save. Also I used **alembic** to migrate in a easy way the tables and **docker-compose**  to setup the database in an easy way.

## Requirements

 - **Docker compose:** Compose is a tool for defining and running multi-container Docker applications. With Compose, you use a YAML file to configure your application’s services. You can read more about docker compose [here](https://docs.docker.com/compose/)
 -  **venv:** The [`venv`](https://docs.python.org/3/library/venv.html#module-venv "venv: Creation of virtual environments.") module provides support for creating lightweight “virtual environments” with their own site directories, optionally isolated from system site directories.

## Installing Project Dependencies
To install the project dependencies you need create a new **virtual enviromen**t with the next command:

     py -m venv venv
After you have to active the **virtual enviroment**  
**Windows**
  

      .\venv\Scripts\activate

 **Mac OS / Linux**
 

    source ./venv/Scripts/activate
    
   And finally you can install the dependencies running this command:
   

    pip install -r requeriments.txt

## Setup Database
To setup the dabase you need open a terminal in the root project folder and run the next command

    docker-compose up -d
This command will create a container with a postgres database, you can access to this database throutgh the **5432 port**.
**Database Information**
 - **user**: postgres
 - **password**: postgres
 - **host name:** postgres
 - **port**: 5432

You can change the database parameters in the **docker-compose.yaml**, also you can change the database connection string in the **.env** file. 
## pgAdmin 4 Setup (Optional)
The last command also will create a container with **pgAdmin 4** to manage the dabase, you can access to pgAdmin 4 with the next link [localhost:5050](http://localhost:5050).
The default login information is:
 - **email:** admin@admin.com
 - **password:** root


## Creating the tables

You can create the tables in a easy way running the next commands:

    alembic revision --autogenerate -m "Creating tables"   
    alembic upgrade heads

   
## ER Diagram

![Alt text](https://github.com/mata649/costa_rica_supermarkets_scrapper/blob/images/ERD%20diagram.png)


## Running ETL Process

    py main.py --help
With the previous command you can see the general information of the program and also the supermarkets that you can choose, at the time of writing this readme, you can choose:

 - pequeno_mundo
 - pricesmart

To choose pequeno_mundo, have to run the next command:

    py main.py --supermarket pequeno_mundo
