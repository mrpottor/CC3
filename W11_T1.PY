
def main() :
    for _ in range(int(input("no of tests ="))):

        n, k = [int(i) for i in input("n and k =").split()]

        x=0

        while n!=0:

            q = n // k

            x += (((n * (n + 1)) // 2) - ((q * (q + 1)) // 2) * k)

            n = q

        print(x)    

if __name__ == "__main__":
    main()