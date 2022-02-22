def l_7_hw_2(a):
    a = int(input('Introduce un numar'))
    for nr in range(2, int(a / 2) + 1):
        if (a % nr) == 0:
            print(a, "not prime')
            break
        else:
            print({a}, 'prime')
