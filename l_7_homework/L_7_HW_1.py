def palindrom(fraza):
    string_a = fraza.lower().replace(' ', '')
    stringlength=len(string_a)
    slicedString=string_a[stringlength::-1]
    if string_a == slicedString:
        return True
    return False

#def palindrom(fraza):
#    fraza = input('Introduce o propozitie:')
#    string_a = fraza.lower().replace(' ', '')
#    stringlength=len(string_a) # calculate length of the list
#    slicedString=string_a[stringlength::-1]
#    if string_a == slicedString:
#        print('da')
#    else:
#        print('nu')