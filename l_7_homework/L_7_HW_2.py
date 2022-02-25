def l_7_hw_2(a):
    a = int(input('Introduce un numar'))
    for nr in range(1, int(a / 2) + 1):
        if (a % 2) == 0:
            print(a,'is not prime')
            break
        else:
            print(a, 'is prime')
            break