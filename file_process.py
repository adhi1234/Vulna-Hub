import json

# read file
with open('parsed_file.json', 'r') as myfile:
    data=myfile.read()

# parse file
obj = json.loads(data)

# show values
print("data: " +str(obj['cve']['CVE_data_meta']['ID']))



