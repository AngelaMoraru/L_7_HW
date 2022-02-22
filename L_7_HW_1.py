def l_7_hw_1():
    user_input = input('Introduce o propozitie:')
    string_a = user_input.lower().replace('', '')
    reversa = string_tools.string_reversed(user_input)
    if string_a == reversa:
        print('da')
    else:
        print('nu')