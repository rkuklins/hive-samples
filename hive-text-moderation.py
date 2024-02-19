# -------------------------- #
# Text API requests

import requests

headers = {
    'Authorization': 'Token YOUR_API_KEY',
}

data = {
  'text_data': 'My input string goes here.',
  'metadata': '{"my_UUID": "3c78fc82-f797-11ea-adc1-0242ac120002"}'
}

response = requests.post('https://api.thehive.ai/api/v2/task/sync',
                          headers=headers, 
                          data=data)

response_string = response.text 
response_dict = response.json()

# -------------------------- #
# submit a task with specified language (speech/text moderation, transcription only)
# see docs for supported language
import requests

headers = {
    'Authorization': 'Token YOUR_API_KEY',
}

files = {'image': open('my_path/my_image.jpg', 'rb')}

data = {
  'metadata': '{"my_UUID": "3c78fc82-f797-11ea-adc1-0242ac120002"}',
  'options': '{"input_language":"es"}'
}

response = requests.post('https://api.thehive.ai/api/v2/task/sync',
                          headers=headers, 
                         	files=files,
                          data=data)

response_string = response.text 
response_dict = response.json()

# -------------------------- #