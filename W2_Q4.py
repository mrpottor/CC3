t = int(input('no of tests:-'))
while t > 0:
    p = int(input('enter prime number:-'))
    a = []
    b = []
    c = 0
    for i in range(1,p):
        a.append(i)
    for i in range(1,p):
        for j in range(1,p):
            b.append((i**j)%p)
        
    print(c)
    print(set(b))
    print(a)
    t -= 1