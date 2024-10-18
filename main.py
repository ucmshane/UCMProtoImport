import csv
import requests

# Define the API endpoint URL
api_url = "https://proto.ucmerced.edu/Services/REST/v1/assignIP4Address"

# Define the configuration ID currently set to UCMerced
configuration_id = 5

#Have to generate this from BAM if you don't already have one yo
authorization_token = "BAMAuthToken: TacoBellIsTheBest"

# Open and read the CSV file
with open("C:\\Options\\protoImport\\venv\\RedNet-Arp.csv", 'r') as csvfile:
    # Create a CSV reader
    csvreader = csv.reader(csvfile)

    # Skip the header row if present
    next(csvreader, None)

    # Loop through the CSV rows
    for row in csvreader:
        # Extract values from the CSV row
        mac_address = row[0].strip()
        ip_address = row[1].strip()
        host_info = row[2].strip()
        property_name = row[3].strip()

        # Headers
        headers = {
            "Authorization": authorization_token
        }

        # Parameters
        params = {
            "configurationId": configuration_id,
            "macAddress": mac_address,
            "ip4Address": ip_address,
            "hostInfo": f"{host_info},4388,false,false",
            "action": "MAKE_STATIC",
            "properties": f"name={property_name}"
        }

        # Make the REST API call with headers
        response = requests.post(api_url, headers=headers, params=params)

        # Check the response status
        if response.status_code == 200:
            print(f"API call successful for IP: {ip_address}")
        else:
            print(f"API call failed for IP: {ip_address}. Error: {response.text}")
