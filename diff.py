N = int(input('no of boxes- '))
B = list(map(int, input('space separated input - ').split()))
odd = 0
even = 0

for i in B:
    if i%2 == 0:
        even = even+i
    else :
        odd = odd+i
if odd > even :
    print(odd-even)
else:
    print(even-odd)