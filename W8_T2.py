import re

s = input('Enter the string:-')
if re.search("^[_a-zA-Z..a-zA-Z]$",s):
    print('valid')
else:
    print('invalid')