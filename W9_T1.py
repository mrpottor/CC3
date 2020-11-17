import string
s = input('Input the string :-')
x = int(input('Value of X:-'))
s = s.lower()
l = list(s)
# 65-90(cap)
# 97-122
for i in s:
    if i in l:
        if l.count(i)%2 == 0:
            if ord(i) + x >= 122 and ord(i) + x >=97:
                l[l.index(i)] = chr(ord(i) + x)
            if ord(i) + x >=122:
                 l[l.index(i)] = chr(97+(122-ord(i) + x))
            if ord(i) + x <=97:
                l[l.index(i)] = chr(122-(97-ord(i) - x))
        else:
            if ord(i) + x >=122:
                 l[l.index(i)] = chr(97+(122-ord(i) + x))
            if ord(i) + x <=97:
                l[l.index(i)] = chr(122-(97-ord(i) - x))
print(l)