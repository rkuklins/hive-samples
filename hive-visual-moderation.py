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
    'Authorization': 'Token 52dVVJa5x0cw3j1wlkcrkS6L28FRiKec',
}

data = {
  'metadata': '{"my_UUID": "3c78fc82-f797-11ea-adc1-0242ac120002"}'
}


# Specify the directory path
directory = '/Users/rafalkuklinski/dev/SC/hive-samples/sample_images/Meds'
root_directory = '/Users/rafalkuklinski/dev/SC/hive-samples/sample_images'

# Get all file names in the directory
file_names = os.listdir(directory)
            
# Process the response
#print(json.dumps(response, indent = 4, sort_keys=True));

# Specify the path of the CSV file
csv_file_name = '/Users/rafalkuklinski/dev/SC/hive-samples/response.csv'

is_first_line = True

json_file_name = '/Users/rafalkuklinski/dev/SC/hive-samples/response.json'
'''
# Open the JSON file in read mode
with open(json_file, 'r') as json_file:
    # Read the content of the file
    response = json.load(json_file)


# Process the response
for reco_class in response['status'][0]['response']['output'][0]['classes']:
    print(str(reco_class['class']) + " -> " + str(reco_class['score']))
#status = response['status'][0]['response']['output'][0]['classes'][3]['class']

'''



# Open the CSV file in write mode
with open(csv_file_name, 'w', newline='') as csv_file:
    # Create a CSV writer object
    writer = csv.writer(csv_file)

    
    # Iterate over each subfolder
    for root, dirs, files in os.walk(root_directory):
        
        # Iterate over each file
        for file_name in files:
            print ("DIR: " + root_directory + " FILE: " + file_name)
            # Construct the file path
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

                #If this is first line, get all the headers and add to the CSV file
                if(is_first_line):
                    is_first_line = False
                    print("CSV Empty: " + str(os.stat(csv_file_name).st_size == 0))
                    line = ["file name"];
                    for reco_class in response_dict['status'][0]['response']['output'][0]['classes']:
                        line.append(str(reco_class['class']))
                        
                    writer.writerow(line)

                # In any case process all the values and add a line
                line = [file_name];
                for reco_class in response_dict['status'][0]['response']['output'][0]['classes']:
                    line.append(str(reco_class['score']))

                writer.writerow(line)   

