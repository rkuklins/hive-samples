# -------------------------- #
# Vision API request for local media files.

import requests
import os
import csv
import json

def get_field_value(json_data, field_name):
    try:
        data = json.loads(json_data)
        value = data[field_name]
        return value
    except (json.JSONDecodeError, KeyError):
        return None
    


headers = { 
    'Authorization': 'Token ov0uxIzXSupNtXHWmmk2poO3gVhZe9IH',
}

data = {
  'metadata': '{"my_UUID": "3c78fc82-f797-11ea-adc1-0242ac120002"}'
}

root = '/Users/rafalkuklinski/dev/SC/hive-samples/sample_images/Drugs'
file_name = 'artworks-GrjdPTS419z6mf3b-KHoQLg-t300x300.jpg'
file_name = 'artworks-000089307630-ov0sw6-t300x300.jpg'


file_path = os.path.join(root, file_name)

# Open the file
with open(file_path, 'rb') as file:
    # Create the files dictionary
    files = {'image': file}
    
    # Make the API request
    response = requests.post('https://api.thehive.ai/api/v2/task/sync', 
                            headers=headers, 
                            files=files,
                            data=data)
    
    # Process the response
    response_dict = response.json() 
    print(json.dumps(response_dict, indent = 4, sort_keys=True))