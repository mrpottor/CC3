n = int(input('no of boxes-'))
p = list(map(int, input('space saperated number-').split()))

even_count = 0
odd_count = 0
for i in p:
    if i%2 == 0:
        even_count = even_count + i
        
    else:
        odd_count = odd_count + i
        

if even_count > odd_count:
    diffs = even_count - odd_count
    print(diffs)
else:
    diffs = odd_count - even_count
    print(diffs)