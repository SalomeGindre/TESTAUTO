import requests
import json

# URL to fetch the data
url = "https://vapi.eumetsat.int/data/search-products/1.0.0/os?format=json&pi=EO:EUM:DAT:METOP:ASCSZF1B&dtstart=2025-02-03T04:41:59Z&dtend=2025-02-04T04:41:59Z"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON content
    data = response.json()
    
    # Extract the required parameters
    extracted_data = []
    for product in data.get('features', []):
        properties = product.get('properties', {})
        extracted_data.append({
            'identifier': properties.get('identifier'),
            'platformShortName': properties.get('platformShortName'),
            'instrumentShortName': properties.get('instrumentShortName'),
            'orbitNumber': properties.get('orbitNumber'),
            'productType': properties.get('productType')
        })
    
    # Print the extracted data
    print(json.dumps(extracted_data, indent=4))
else:
    print(f"Failed to retrieve data. HTTP Status code: {response.status_code}")