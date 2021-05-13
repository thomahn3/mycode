import os
import time

home = os.path.expanduser('~')
localtime = time.ctime()

with os.scandir(str(home) + '/Documents/Text books 9') as entries:
    for entry in entries:
        print(entry.name)

#with open('data.txt', 'r') as f:
 #   data = f.read() 