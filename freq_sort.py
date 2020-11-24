T = int(input())
while T > 0:
    i = input()
    i = list(i)
    i = sorted(i)
    for x in i:
        print(x,end='')
    print("")
    T -= 1