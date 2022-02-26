def perfect_nr(b):
    sum = 0
    for nr in range(1, (b // 2) + 1):
        if b % nr == 0:
            sum += nr
    if sum == b:
        return True
    else:
        return False

#def perfect_list(list):
#    nr_list = []
    #    b = 2
        #    while b > 1 and len(nr_list) < b:
        #        if is_perfect(b):
        #            nr_list.append(b)
    #        b += 2
#    return nr_list