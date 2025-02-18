import requests
import certifi
import xml.etree.ElementTree as ET # used to parse and work with XML
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/extract_parameters', methods=['GET'])
def extract_parameters():
    # URL to fetch the data
    url = "https://vapi.eumetsat.int/data/search-products/1.0.0/osdd?pi=EO:EUM:DAT:METOP:ASCSZF1B"

    # Send a GET request with the certifi CA bundle
    response = requests.get(url, verify=certifi.where())

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the XML content
        root = ET.fromstring(response.content)
        
        # Print the XML content for debugging
        print(ET.tostring(root, encoding='utf8').decode('utf8')) #If the request is successful, this line parses the XML content of the response and creates an ElementTree object
        
        # Define the parameters to extract
        parameter_names = [
            'start', 'end', 'bbox', 'lat', 'lon', 'platform', 'instrument'
        ]
        
        # Extract parameters and store them in a dictionary
        parameters = {}
        for param_name in parameter_names:
            param = root.find(f'.//{param_name}')
            if param is not None:
                parameters[param_name] = param.text
            else:
                parameters[param_name] = None
        
        # Print the parameters dictionary for debugging
        print(parameters)
        
        # Return the parameters as a JSON response
        return jsonify(parameters)
    else:
        return jsonify({"error": f"Failed to retrieve data. HTTP Status code: {response.status_code}"}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)