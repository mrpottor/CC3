count = dict()
name = list(map(str, input().split()))

for i in name:
    count[i] = count.get(i, 0)+1

print(count)
for i in count:
    print(f"{i} count {count.get(i)} times")