def l_7_hw_1(reversa):
    user_input = input('Introduce o propozitie:')
    string_a = user_input.lower().replace(' ', '')
    stringlength=len(string_a) # calculate length of the list
    slicedString=string_a[stringlength::-1]
    if string_a == slicedString:
        print('da')
    else:
        print('nu')