T = int(input("how many tests you want to bro 😎\n"))
# taking input for no of test cases 
while T > 0: # while loop to iterate through tests
    word = input("enter the word bro:-\n")# TAKING word input 
    word = list(word) # converting words to list
    count = dict() # declaring an empty dictionary
    for i in word:
        count[ i ] = count.get(i , 0) + 1
    for i in count:
        print(f"{i}-{count.get(i , 0)}" , end=' ')
    print("")
    T -= 1
