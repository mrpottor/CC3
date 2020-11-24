def printDivisors(n):
    i = 1
    a = {1}
    while i <= n:
        if n % i == 0:
            a.add(i) ,
        i = i + 1
    return a


count = 0
print(printDivisors(3150))

s = printDivisors(int(input('number-')))
s.remove(1)
for i in s:
    if i * i in s:
        count = count + 1
print(len(s)-3+count)
