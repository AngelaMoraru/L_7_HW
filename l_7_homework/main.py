from L_7_HW_1 import palindrom
from L_7_HW_2 import prime
from L_7_HW_3 import perfect_nr

print("Which exercise would you like to test? \n "
      "1: To check if a string is a Palindrome \n "
      "2: To check if a number is prime \n "
      "3: To find a perfect number \n ")

exercise_number = input('Enter a number: ')

if exercise_number == '1':
    fraza = input('Introduce o propozitie:')
    if palindrom(fraza):
        print(f'{fraza} is a palindrome')
    else:
        print(f'{fraza} is not a palindrome')

if exercise_number == '2':
    a = int(input('Introduce un numar: '))
    if prime(a):
        print(f'{a} is a prime number')
    else:
        print(f'{a} is not a prime number')

if exercise_number == '3':
    b = int(input('Introduce un numar: '))
    if perfect_nr(b):
        print(f'{b} is a perfect')
    else:
        print(f'{b} is not perfect')
