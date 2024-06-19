import pandas as pd
from pandas import json_normalize
import json
 
# Load the JSON file
json_file_path = 'fedex.json'
with open(json_file_path, 'r') as f:
    data = json.load(f)
 
# Normalize the nested JSON
df = json_normalize(data)

# Define new data for additional columns
repodf = pd.DataFrame(data, columns = ['repository.name'])
column_data=[]
eaiNumber=[]
column_data=df['repository.name'].tolist()
for reponame in column_data: 
    eaiData=reponame.split("-")
    eaiNumber.append(eaiData[1])
    #print(eaiNumber)


# Add multiple columns using dictionary assignment
new_data = {'EAI Number': eaiNumber}
df = df.assign(**new_data)

#print(df)
# Convert the DataFrame to a CSV file
csv_file_path = 'code-scanning-results.csv'
df.to_csv(csv_file_path, index=False)
 
print(f"Nested JSON file has been converted to CSV file at: {csv_file_path}")
