t = int(input('no of tests'))
while t > 0 :
    a, b, c, m, p = (int(x) for x in input('a, b, c, m, p').split())
    """
    a = no of medicines 
    b = fist power 
    c = second power
    m = no of poor countries
    p = reach countries 
    
    """
    med = a**b
    med = med**c
    earn = (med%m)*p
    if earn == 0:
        print('NO')
    else:
        print(f'YES {earn}')
    t -= 1
