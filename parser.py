from os import listdir
from os.path import isfile, join
import os 
import zipfile
import json



def cve_parse():
    

    files = [f for f in listdir("nvd/") if isfile(join("nvd/", f))]
    files.sort()
    for file in files:
        archive = zipfile.ZipFile(join("nvd/", file), 'r')
        jsonfile = archive.open(archive.namelist()[0])
        cve_dict = json.loads(jsonfile.read())
        jsonfile.close()

    print("CVE_data_timestamp: " + str(cve_dict['CVE_data_timestamp']))
    print("CVE_data_version: " + str(cve_dict['CVE_data_version']))
    print("CVE_data_format: " + str(cve_dict['CVE_data_format']))
    print("CVE_data_numberOfCVEs: " + str(cve_dict['CVE_data_numberOfCVEs']))
    print("CVE_data_type: " + str(cve_dict['CVE_data_type']))



    print("Lets get the data")


    choice=int(input("Lets input a choice"))

#print(json.dumps(cve_dict['CVE_Items'][choice], sort_keys=True, indent=4, separators=(',', ': ')))

    f=open("parsed_file.json","w")
    f.write(json.dumps(cve_dict['CVE_Items'][choice], sort_keys=True, indent=4, separators=(',', ': ')))
    f.close()





    
        




