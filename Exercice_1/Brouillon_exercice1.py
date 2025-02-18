import requests
import xml.etree.ElementTree as ET 

# URL to fetch the data
url = "https://vapi.eumetsat.int/data/search-products/1.0.0/osdd?pi=EO:EUM:DAT:METOP:ASCSZF1B"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the XML content
    root = ET.fromstring(response.content)
    
    # Define the parameters to extract
    parameter_names = [
        'start', 'end', 'bbox', 'lat', 'lon', 'platform', 'instrument'
    ]
    
    # Extract and print the parameters
    for param_name in parameter_names:
        param = root.find(f'.//{param_name}')
        if param is not None:
            print(f"{param_name}: {param.text}")
        else:
            print(f"{param_name}: Not found")
else:
    print(f"Failed to retrieve data. HTTP Status code: {response.status_code}")