
def removeDubbled(x):
    t="" 
    for i in x: 
        if(i not in t): 
            t=t+i
    return t


def main():
    a = input("Enter the string:-")
    print(removeDubbled(a))

if __name__ == "__main__":
    main()