
T = int(input('no of tests'))
for i in range(T):

    s , p = (str(x) for x in input().split())
    
    l1 = len(s)
    l2 = len(p)
    if l2 == 2*(l1):
        if s in p:
            print("Possible")
    else:
        print('impossible')

    




