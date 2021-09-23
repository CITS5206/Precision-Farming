
"""
This function searches a file or folder from the system and returns a file path


Test Cases:
 1. Input: 
      - Enter any filename (with correct case) without extension but is in the directory e.g Documents
      - Enter any filename (with wrong letter case) without extension but is in the directory e.g documents
      - Enter any filename with extension but is in the directory e.g main.py
      - Enter a file that is not in the directory, it should output "File not found in the dir"

"""

import os

#function that searches for the file in the dir
def find_files(filename, search_path):
   result = []

# Wlaking top-down from the root
   for root, dir, files in os.walk(search_path):
      if filename in files:
         result.append(os.path.join(root, filename))
   
   if not result:
         return ("File is not found in this directory")
   else:
      return ("Directory of the file: ",result)



#function that searches for the folder in the dir
def find_folder(filename, search_path):
   result = []

# Wlaking top-down from the root
   for root, dir, files in os.walk(search_path):
      if filename in dir:
         result.append(os.path.join(root, filename))
   
   if not result:
         return ("File is not found in this directory")
   else:
      return ("Directory of the file: ",result)



#function that checks file extension, if there is extension, then the input is a file, else input is folder
def checkfile_extension(file):
   name, extension = os.path.splitext(file)
   #print("Name of File: ",name, "exention is: ",extension)

   if not extension: #if extension is empty
      #print("Filename is a folder")
      print(find_folder(file,"."))
      
   else:
      #print("Filename is a file")
      print(find_files(file,"."))


### Main ####

var = input("Enter filename: ")
checkfile_extension(var)
