import re
#open the xml file for reading:]


newdata="test3"
with open('test.txt','r+') as f:
    #convert to string:
    data = f.read()
    f.seek(0)
    f.write(re.sub(newdata,data))
    f.truncate()