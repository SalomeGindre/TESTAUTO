# TESTs AUTO

## Prerequisites

- Python 3.0
- Request library
- Certifi library
- Flask
- BeautifulSoup

WARNING : 
If you have the ERROR SSLError, install : 
> pip install pip-system-certs 

from this source : https://stackoverflow.com/questions/77442172/ssl-certificate-verify-failed-certificate-verify-failed-unable-to-get-local-is

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

### PART 1
This exercice provides a Python script to extract specific parameters from an XML response obtained from the EUMETSAT API and serve the extracted data as a JSON response via a Flask web server.

**Running the Script**

Run the Flask app : 

> python app.py

Access the JSON response by navigating to : 
* http://127.0.0.1:5000/extract_parameters 

in your web browser or using a tool like curl or Postman. 
(The part 1 is not properly yet working, the app is working the parameters are still null)

### PART 2

Extract below parameters for the available products from the search results for this query https://vapi.eumetsat.int/data/search-products/1.0.0/os?format=json&pi=EO:EUM:DAT:METOP:ASCSZF1B&dtstart=2025-02-03T04:41:59Z&dtend=2025-02-04T04:41:59Z

* properties.identifier
* platformShortName
* instrumentShortName
* orbitNumber
* productType

**Running the Script**

Run the Flask app : 

> python app2.py

Access the JSON response by navigating to : 
* http://127.0.0.1:5000/extract_parameters2 

in your web browser or using a tool like curl or Postman.

## Exercice 2

This exercice involves programmatically retrieving and processing satellite product data from the EUMETSAT data repository. The goal is to count the number of products available on a specific date and extract their identifiers and details, then save this information to a CSV file.

To run the script and get the CSV file, write in your terminal: 
> python product.py

The Python script performs the following actions:

* Sends a GET request to the specified URL.
* Parses the HTML content to find all product hyperlinks.
* Filters the products to include only those starting with "ASCA".
* Writes the product names and links to a CSV file.

## Exercice  3

The goal of this exercice is to track the events that each product went through in a series of backend services after being sent via HTTP POST. Each product is assigned a unique identifier by the first service, and this identifier is used by subsequent services to log their actions.

