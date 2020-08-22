# Projet 8: PurBeurre

## Description

The goal of this project is to create a web application which interacts with the Open Food Facts products database.

The application uses the API from Open Food Fact to download a bunch of products classified by categories.

Once the products are downloaded the application fills a PostgreSQL database with the data.

Then, a user can launch the program, choose a product from different categories and the program will compare and propose a substitute to the product.
The substitute is a product healthier than the selected product.

The user can also safe the substitute in the database.

## Language

* Python

## Framework

* Django

## Requirements

Use the following command in terminal to install requirements:

```
pip install -r requirements.txt
```

## Features

* Look up for products in Open Food Facts database;
* CLI application;
* The user interacts with the application in the console;
* The user can choose a product and get a substitute with a better nutriscore;
* The user can save a product and his substitute in the db;
* The user can consult products saved in db;


## Prerequisite

First, it is necessary to download and install Postgresql. Then create a local Postgresql database. (https://www.postgresql.org/download/)

On MacOs you can install Homebrew (a packet manager): https://brew.sh/index and then in a terminal: brew install postegresql

Once the database is created, you can fill the connection information in the following file: config\settings.py

Example:
```
 DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'django_project_8',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}
```


## Installation

To creates the tables in the database with the data from Open Food Facts, you have to run this command:

```
python manage.py populate_db initialize
```

By default, the application download data from OFF with a page size of: 1000.
You can edit this configuration here: config\settings.py

## Launch the app

To launch the application, run this command:

```
python manage.py runserver
```