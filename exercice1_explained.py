import requests # used to send HTTP request in Python
import xml.etree.ElementTree as ET # used to parse and work with XML
import certifi

# URL to fetch the data
url = "https://vapi.eumetsat.int/data/search-products/1.0.0/osdd?pi=EO:EUM:DAT:METOP:ASCSZF1B"

# Send a GET request with the certifi CA bundle
response = requests.get(url, verify=certifi.where())
print(response)

# Check if the request was successful
if response.status_code == 200:
    # Parse the XML content
    root = ET.fromstring(response.content) #If the request is successful, this line parses the XML content of the response and creates an ElementTree object
    print(root)
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