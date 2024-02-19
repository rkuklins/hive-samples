# -------------------------- #
# Vision API request for local media files.

import requests

headers = { 
    'Authorization': 'Token 52dVVJa5x0cw3j1wlkcrkS6L28FRiKec',
}

files = {'image': open('sample_files/porno4.png', 'rb')}

data = {
  'metadata': '{"my_UUID": "3c78fc82-f797-11ea-adc1-0242ac120002"}'
}

response = requests.post('https://api.thehive.ai/api/v2/task/sync', 
                         headers=headers, 
                         files=files,
                         data = data)

response_string = response.text 
response_dict = response.json()


print("Response string: ", str(response_dict));
