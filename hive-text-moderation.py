# -------------------------- #
# Text API requests

import requests
import csv

# Specify the path of the CSV file
csv_input_file_name = '/Users/rafalkuklinski/dev/SC/hive-samples/sample_texts/random_texts.csv'
csv_output_file_name = '/Users/rafalkuklinski/dev/SC/hive-samples/sample_texts/hive_response_random.csv'

is_first_line = True



headers = {
    'Authorization': 'Token p5CtNSI2XSmdzfs1E1o2fypuaW0yQ1gE',
}

data = {
  'text_data': 'Suck My Pussy Nigga Every Opp Shot Nigga Gang Gang Nigga',
  'metadata': '{"my_UUID": "3c78fc82-f797-11ea-adc1-0242ac120002"}'
}

texts = []
text_no=0;

# Load CSV file into a structure
with open(csv_input_file_name, 'r') as file:
  reader = csv.reader(file)
  for row in reader:
    texts.append(row[0])  # Assuming the text is in the first column of the CSV

# Open the CSV file in write mode
with open(csv_output_file_name, 'w', newline='') as csv_file:
  # Create a CSV writer object
  writer = csv.writer(csv_file)
  # Iterate over all texts in the sample file
  for text in texts:
    print("Text [" + str(text_no) + "]:" + text)
    text_no = text_no + 1;
    
    #Each text from a file add to the "data" structure for hive request
    data['text_data'] = text

    # Make the API request to hive
    response = requests.post('https://api.thehive.ai/api/v2/task/sync',
                headers=headers,
                data=data)

    # Process the response
    response_string = response.text
    response_dict = response.json()

    try:
        #If this is first line, get all the headers and add to the CSV file
        if(is_first_line):
            
            line = ["file name", "text"];
            for reco_class in response_dict['status'][0]['response']['output'][0]['classes']:
                line.append(str(reco_class['class']))
                
            writer.writerow(line)
            is_first_line = False

        # In any case process all the values and add a line
        line = [csv_input_file_name, text];
        for reco_class in response_dict['status'][0]['response']['output'][0]['classes']:
            line.append(str(reco_class['score']))

        writer.writerow(line)   
    except:
        print("Error processing: " + file_name)
# -------------------------- #