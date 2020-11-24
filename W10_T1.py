
t = int(input('no of test cases :-'))
for i in range(t):
    f = list(map(str,input('formula :').split()))
    if f[0].isdigit() and f[2].isdigit():
        print(int(f[0])+int(f[2]))
    elif f[0].isdigit() and f[4].isdigit():
        print(int(f[4])-int(f[0]))
    elif f[2].isdigit() and f[4].isdigit():
        print(int(f[4])-int(f[2]))