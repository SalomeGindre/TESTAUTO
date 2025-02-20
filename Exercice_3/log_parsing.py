"""
This script will extract and list the events for each product based on its unique identifier.   
Steps to solve the exercice : 1. extract unique identifier, 2. track events in each service, list events 

Task : Using the unique identifier, you need to list the events that each product went through in each service. This involves parsing log files to extract relevant information.
"""
import re

# Function to parse a log file and extract events for a given identifier
def parse_log(file_path, identifier):
    events = []
    with open(file_path, 'r') as file:
        for line in file:
            if identifier in line:
                events.append(line.strip())
    return events

# Unique identifier for the product
identifier = "753be839-7007-41ad-9e62-cf5a1549499c"

# Log files
log_files = [
    "olda-ingestion-gateway-normal-0.log",
    "olda-ingestion-processing-normal-0.log",
    "olda-storage-manager-normal-65b44774cc-szgsn.log",
    "olda-ingestion-housekeeping-normal-57cf8dd646-kh824.log"
]

# Parse each log file and collect events
all_events = {}
for log_file in log_files:
    all_events[log_file] = parse_log(log_file, identifier)

# Print the events
for log_file, events in all_events.items():
    print(f"Events in {log_file}:")
    for event in events:
        print(event)