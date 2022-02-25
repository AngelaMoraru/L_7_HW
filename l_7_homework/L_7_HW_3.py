def l_7_hw_3(perfect):
    perfect = int(input('Introduce un numar'))
    sum = 0
    for nr in range(1, (perfect // 2) + 1):
        if perfect % nr == 0:
            sum += nr
    if sum == perfect:
        print(perfect, 'is perfect')
    else:
        print(perfect, 'is not perfect')