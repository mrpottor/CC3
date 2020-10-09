import re
import sys
password = input('Enter password\n')
flag = 0
if len(password) < 6:
    print(f'Please enter {6-len(password)} more characters')
    sys.exit()
else:
    while True:
        if not re.search("[a-z]", password): 
            flag = -1
            break
        elif not re.search("[A-Z]", password): 
            flag = -1
            break
        elif not re.search("[0-9]", password): 
            flag = -1
            break
        elif not re.search("[_@$#%*^&]", password): 
            flag = -1
            break
        elif re.search("\s", password): 
            flag = -1
            break
        else: 
            flag = 0
            print("Strong password")
            break
    if flag == -1:
        print("weak password")