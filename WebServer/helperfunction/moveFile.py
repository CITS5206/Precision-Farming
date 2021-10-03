# -------------------------------------------
# Function:
#   1. move file
#   2. move folder
# -------------------------------------------



import os
import shutil
from tkinter import *

# change the srcDir and fileName to the file / folder need to be moved
# change the DESTINATION_DIR to where to folder / file need to be moved to

# srcDir using funcion2 to find the path of the file?
srcDir = '/Users/mha/Desktop/MoveFiles/OriginDir'
fileName = 'test.csv'

# the path we need the file to be
DESTINATION_DIR = '/Users/mha/Desktop/MoveFiles/DestinationDir'

window = Tk()
window.title("Precision Farming App")
window.geometry('1024x614')

lbl_moveFile = Label(window, text="{}/{}".format(srcDir, fileName))
lbl_moveFile.grid(column=0, row=0)

lbl_moveFolder = Label(window, text="{}".format(srcDir))
lbl_moveFolder.grid(column=0, row=1)


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
        print(outTxt)
        lbl_moveFile.configure(text=outTxt)
    except FileNotFoundError as e:
        lbl_moveFile.configure(text=e)

# Move folder
    # if the folder exists in destination folder, delete the the existing folder
    # and move the folder into the desination
def moveFolder(srcDir):
    try:
        folder = srcDir[srcDir.rfind('/')+1:]
        newPath = shutil.move(srcDir, DESTINATION_DIR)
        outTxt = f'{folder} have been move to {newPath}'
        lbl_moveFolder.configure(text=outTxt)
    except shutil.Error:
        shutil.rmtree(f'{DESTINATION_DIR}/{folder}')
        print(f'Deleted: {DESTINATION_DIR}/{folder}')
        newPath = shutil.move(srcDir, DESTINATION_DIR)
        outTxt = f'{folder} have been move to {newPath}'
        lbl_moveFolder.configure(text=outTxt)
    except FileNotFoundError as e:
        lbl_moveFolder.configure(text=e)


btn_movFile = Button(window, text="Move file", command=lambda: moveFile(srcDir, fileName))
btn_movFile.grid(column=1, row=0)
btn_movFolder = Button(window, text="Move folder", command=lambda: moveFolder(srcDir))
btn_movFolder.grid(column=1, row=1)


window.mainloop()
