# TESTs AUTO

## Prerequisites

- Python 3.0
- Request library
- Certifi library
- Flask

## Set up

1. Create a Virtual Environment

It's recommended to create a virtual environment to manage dependencies.

***bash***
> pip install virtualenv \
> virtualenv venv

2. Activate the environment

> venv\Scripts\activate

3. Install Required Libraries

> pip install -r requirements.txt


## Exercice 1

This project provides a Python script to extract specific parameters from an XML response obtained from the EUMETSAT API and serve the extracted data as a JSON response via a Flask web server.

**Running the Script**

Run the Flask app : 

> python app.py

Access the JSON response by navigating to : 
* http://127.0.0.1:5000/extract_parameters 

in your web browser or using a tool like curl or Postman.

