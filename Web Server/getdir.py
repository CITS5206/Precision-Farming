from os import walk
import os
f = []
for (dirpath, dirnames, filenames) in walk(os.getcwd()):
    f.extend(filenames)
print(f)