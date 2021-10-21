"""
Author: Clariza Look
This program reads a csv file from combined data of sensor and gps. 
It will generate a json file format out from the csv file
"""

import os
import csv
import json
import re

#checks if input file has contents
def check_file_content(f):
   # check if size of file is 0
   content = open(f, 'r').read()
   if re.search(r'^\s*$', content):
      return True #true if file has no content
   else:
      return False #true if file has content

     
# Function to convert list to string 
def listToString(s): 
    
    # initialize an empty string
    str1 = "" 
    
    # traverse in the string  
    for ele in s: 
        str1 += ele  
    
    # return string  
    return str1 
        

#function that searches for the file in the dir
def find_files(filename, search_path):
   result = []

# Walking top-down from the root
   for root, dir, files in os.walk(search_path):
      if filename in files:
         result.append(os.path.join(root, filename))
   
      return (result)

 
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
         

### MAIN CODE ####
 
#Step1:  Set the two files needed for the program
csv_file = r'DUALEM-orignal.csv' #this file is coming from the combined dualem and gps data given by Hira
json_file = r'dualem-output3.json' #this will be the converted json file. This creates the file name if json file is not present
 
#Step2: check if file is present in the current directory where .py is located
file_status  = find_files(csv_file, '.') 

if not file_status:
   print("Csv file does not exist the directory. Please input another that in the directory")

else:
   #Step 3: If file is in the directory, get directory of file

   #convert file_status type to string format
   csv_file_path = listToString(file_status)
  
   
   #Step 4: check if file has content
   if not check_file_content(csv_file_path):
      #then call the convert_to_json function
      convert_to_json(csv_file_path , json_file)
   else:
      print('File has empty contents')

  
   