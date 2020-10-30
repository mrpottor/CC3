
def is_prime(n):
    if n<= 0:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True


def sum_of_prime(n):
    P = []
    for i in range(2,n+1):
        if is_prime(i):
            P.append(i)
    return sum(P)


def main():
    t = int(input("no of test:-"))
    for i in range(t):
        x = input('binary string:- ')
        x = int(x,2)
        print(sum_of_prime(x))



if __name__ == '__main__':
    main()