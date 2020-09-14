T = int(input())

N , X = (int(x) for x in input().split())

for i in range(1,N):
    X = X*i

print(X)