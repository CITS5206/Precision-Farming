import time
f1 = open("dualem-data.txt",'r')
f2 = open("gps-data.txt",'r')
dualem = iter(f1.readlines())
gps = iter(f2.readlines())
f1.close()
f2.close()

while True:
    print(dualem.__next__())
    time.sleep(1)
    