# Trips

### Features

There must be an automated process to ingest and store the data.

● Trips with similar origin, destination, and time of day should be grouped together.

● Develop a way to obtain the weekly average number of trips for an area, defined by a
bounding box (given by coordinates) or by a region.

● Develop a way to inform the user about the status of the data ingestion without using a
polling solution.

● The solution should be scalable to 100 million entries. It is encouraged to simplify the
data by a data model. Please add proof that the solution is scalable.

● Use a SQL database.

## Requirements

* `requirements.txt`

## Starting the Database
* Type the following docker command in the terminal:
```
sudo docker-compose up -d
```
* To access the database the secrets used are:

```
POSTGRESQL_USER='postgres'
POSTGRESQL_PASSWORD='postgres'
POSTGRESQL_HOST='localhost'
POSTGRESQL_PORT=5432
POSTGRESQL_DB='postgres'
```

## Starting the process

Install the requirements
```
pip install -r requirements.txt
```

## Data Ingestion to Postgresql

Run the script to upload the data, generate the view, select the data and export to csv
```
python csvs/data_import.py
```

## Features
Run the command to open the jupyter notebook with the informations about the features and the architecture
```
jupyter notebook
```

## Informations:

The python script `csvs/data_import.py` has the following functions:
- `upload_csv_sql`: used to upload the csv files to the postgresql database;
- `data_transform`: used to manipulate the data from the dataframe;

The python script `utils/dataviz.py` has the following functions:
- `plot_geolocation_by_cluster`: Function to plot latitude and longitude coordinates;
