# -------------------------------------------
# Test
#   1. Right place
#   2. Right Content
# -------------------------------------------

import os
import shutil
import hashlib

srcDir = '/Users/mha/Desktop/test_move'
srcSubDir = '/Users/mha/Desktop/test_move/subDir'
DESTINATION_DIR = '/Users/mha/Desktop/test_move/DestinationDir'
DESTINATION_SUB_DIR = '/Users/mha/Desktop/test_move/DestinationDir/subDir'


# test functions
def createFile(dirName, fileName):
    with open(f'{dirName}/{fileName}', 'w') as f:
        f.write('Hello,world\nHappy,coding')

def get_file_hash(file):
    BLOCK_SIZE = 65536              # The size of each read from the file
    file_hash = hashlib.sha256()    # Create the hash object, can use something other than `.sha256()` if you wish
    with open(file, 'rb') as f:     # Open the file to read it's bytes
        fb = f.read(BLOCK_SIZE)     # Read from the file. Take in the amount declared above
        while len(fb) > 0:          # While there is still data being read from the file
            file_hash.update(fb)    # Update the hash
            fb = f.read(BLOCK_SIZE) # Read the next block from the file
    return(file_hash.hexdigest())


        

# move file from one directory to another
    # if file exitst
        # tell the user it would be replaced and replace it
def moveFile(dirName, fileName):
    if os.path.exists(f'{DESTINATION_DIR}/{fileName}'):
        print(f'{fileName} already exists in {DESTINATION_DIR}, it would be replaced')
    # specifing file name in destination directory, file would be replaced 
    # otherwise shutil.Error rasied
    try:
        newPath = shutil.move(f'{dirName}/{fileName}', f'{DESTINATION_DIR}/{fileName}')
        outTxt = f'{fileName} have been moved to {newPath}'
        # print(outTxt)
    except FileNotFoundError as e:
        print(e)

# Move folder
    # if the folder exists in destination folder, delete the the existing folder
    # and move the folder into the desination
def moveFolder(srcDir):
    try:
        folder = srcDir[srcDir.rfind('/')+1:]
        newPath = shutil.move(srcDir, DESTINATION_DIR)
    except shutil.Error:
        shutil.rmtree(f'{DESTINATION_DIR}/{folder}')
        # print(f'Deleted: {DESTINATION_DIR}/{folder}')
        newPath = shutil.move(srcDir, DESTINATION_DIR)
        # outTxt = f'{folder} have been move to {newPath}'
    except FileNotFoundError as e:
        print(e)

def main():
    # Create a test folder
    os.mkdir(srcDir)
    os.mkdir(DESTINATION_DIR)

    # create file in folder
    createFile(srcDir, 'test.csv')

    # Create sub folder
    os.mkdir(srcSubDir)
    # Create two files in sub folder
    createFile(srcSubDir, 'sub1.csv')
    createFile(srcSubDir, 'sub2.csv')

    # test move file
    # get origin file hash
    srcHash = get_file_hash(os.path.join(srcDir,'test.csv'))
    
    # move file
    moveFile(srcDir,'test.csv')
    
    # test target file exists
    if os.path.exists(os.path.join(DESTINATION_DIR,'test.csv')):
        print('OK - Test 1 - Move File')
    else:
        print('Failed - Test 1 - Move File')
    
    # test target file content
    targetHash = get_file_hash(os.path.join(DESTINATION_DIR,'test.csv'))
    if srcHash == targetHash:
        print('OK - Test 2 - File content correct')
    else:
        print('Failed - Test 2 - File content incorrect')

    # test move folder
    srcHash = get_file_hash(os.path.join(srcSubDir,'sub1.csv'))
    moveFolder(srcSubDir)
    targetHash = get_file_hash(os.path.join(DESTINATION_SUB_DIR,'sub1.csv'))
    # test target floder exists
    if os.path.exists(DESTINATION_SUB_DIR) and \
    os.path.exists(os.path.join(DESTINATION_SUB_DIR,'sub1.csv')) and\
    os.path.exists(os.path.join(DESTINATION_SUB_DIR,'sub2.csv')):
        print('OK - Test 3 - Move Folder')
    else:
        print('Failed - Test 3 - Move Folder')

    # test target file content
    if srcHash == targetHash:
        print('OK - Test 4 - Folder File content correct')
    else:
        print('Failed - Test 4 - Folder File content incorrect')
    
    # Clean test folder
    shutil.rmtree(srcDir)


if __name__ == '__main__':
    main()