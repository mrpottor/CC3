import re

t = int(input('no of tests:-'))

for i in range(t):
    s = input('enter the string :-')
    if len(s) < 26:
        print('NO')
    if re.findall("[a-zA-Z]",s):
        print('NO')