def perfect_nr(b):
    sum = 0
    for nr in range(1, (b // 2) + 1):
        if b % nr == 0:
            sum += nr
    if sum == b:
        return True
    else:
        return False

