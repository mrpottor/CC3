def factorial(n):
    if n < 0:
        print('invalid input.')
        return
    # single line to find factorial
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1);


n = int(input('enter the number'))
fact = factorial(n)
fact = str(fact)
fact = fact.replace('0','')
print(fact[-1])