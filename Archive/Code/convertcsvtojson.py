"""
This program reads a csv file from combined data of sensor and gps. 
It will generate a json file format out from the csv file

"""


import csv
import json
 
 
# Function to convert a CSV to JSON
# Takes the file paths as arguments
def convert_to_json(csvfile, jsonfile):
     
    # creating a dictionary
    data = {}
     
    # Open a csv reader called DictReader
    with open(csvfile, encoding='utf-8') as cf:
        csvReader = csv.DictReader(cf)
         
        # Convert each row into a dictionary
        # and add it to data
        for rows in csvReader:
             
            # The column named 'Latd' to
            # be the primary key
  
            key = rows['LATd']
            data[key] = rows
 
    # Open a json writer, and use the json.dumps()
    # function to dump data
    with open(jsonfile, 'w', encoding='utf-8') as jf:
        jf.write(json.dumps(data, indent=2))
         
# MAIN CODE
 
# The two files needed for the program
csv_file = r'dualem.csv'
json_file = r'output.json' #creates if json file is not present
 
# Call the make_json function
convert_to_json(csv_file, json_file)