count = dict()
line = input('enter the line- ')
words = line.split()

print("counting....")
for word in words:
    count[word] = count.get(word,0) + 1
print('counts.....\n',count)
