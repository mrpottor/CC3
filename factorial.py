def factorial(n):
    if n < 0:
        print('invalid input. ^_^')
        return
    # single line to find factorial
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1);




def main():
    c = int(input('enter the number which factorises '))
    print(factorial(c))


if __name__ == '__main__':
    main()