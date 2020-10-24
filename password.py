import re
T = int(input('no of tests\n'))
for i in range(T):

    s , p = (str(x) for x in input('enter string and password :-').split())
    if len(p) == 2*(len(s)):
        if re.search(s,p):
            print("possible")
    else:
        print('impossible')

    




