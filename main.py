import requests
import json
 
# Define your data payload
data = [
    {"field1": "value1", "field2": 123},
    {"field1": "value2", "field2": 456}
]
 
# Define the streaming data URL
streaming_data_url = 'https://api.powerbi.com/beta/b945c813-dce6-41f8-8457-5a12c2fe15bf/datasets/5217901d-3f4b-4784-ad59-8555293df382/rows?referrer=desktop&experience=power-bi&key=zjvLqHTXBFtyRax6PVKPg9JWxg1dPRVe0q3zKYMRi9tpnu7UUnaChajaax5No0R2BxC2wIQWJLtrPADqVphMQA%3D%3D'
 
# Send data to Power BI
headers = {'Content-Type': 'application/json'}
response = requests.post(streaming_data_url, headers=headers, data=json.dumps(data))
 
# Check response status
if response.status_code == 200:
    print('Data sent successfully to Power BI')
else:
    print('Failed to send data to Power BI:', response.status_code)
