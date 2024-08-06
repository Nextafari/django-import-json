## Apexive Pilot Log Importer and Exporter

#### Project Overview
This project, named Apexive, is a Django application designed to import pilot log data from a JSON file and export it to a CSV format. The project uses Django Rest Framework (DRF) for API creation and SQLite for the database.

Features
Importer Module: Reads data from a JSON file and stores it in the database.
Exporter Module: Exports data from the database to a CSV file in a specified format.
Both the importer and exporter use django management commands to achieve this.

#### Installation

##### Clone the repository

```bash
git clone https://github.com/yourusername/apexive.git

cd apexive
```

##### Setup Virtual Environment

Create a virtual environment and activate it eg:

```bash
pipenv shell
```

##### Install Dependencies

Install the required dependencies using pip:

```bash
pip3 install -r requirements.txt
```

##### Apply Migrations

Run the following commands to apply the migrations:

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

##### Configuration

Pre-commit Hooks
To ensure code quality, pre-commit hooks are used. Install the pre-commit hooks with:

```bash
pre-commit install
```

##### Start up the Server

Start the Django development server:

```bash
python3 manage.py runserver
```

----

#### Importer Module

To import data from the JSON file Data/import - pilotlog_mcc.json, use the Django management command:

```bash
python3 manage.py import_data
```

----

#### Exporter Module

To export data to a CSV file in the format specified in export-logbook_template.csv, use the following management command:

```bash
python3 manage.py export_data
```
