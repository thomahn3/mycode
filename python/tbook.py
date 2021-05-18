import os
import time
from datetime import datetime 
import calendar

#variables
home = os.path.expanduser('~')
#print
timern = datetime.now().time()

dayrn = datetime.now().weekday()



#if statements
if dayrn == 0: 
    print("monday")
elif dayrn == 1:
    print("tuesday")
elif dayrn == 2:
    print("wednesday")
elif dayrn == 3:
    print("thursday")
elif dayrn == 4:
    print("friday")
elif dayrn == 5:
    print("saturday")
elif dayrn == 6:
    print("sunday")

with os.scandir(str(home) + '/Documents/Text books 9') as entries:
    for entry in entries:
        print(entry.name)

#with open('data.txt ', 'r') as f:
 #   data = f.read() 