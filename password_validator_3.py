from checks import *

password = input("Bitte Password eingeben: ")
symbol_list = ["-","?","!","#","_"]
length = 8

lower_check = function_lowercase(password)
upper_check = function_uppercase(password)
digit_check = function_digit(password)
symbol_check = function_symbol(password, symbol_list)
length_check = function_minlength(password, length)

if not length_check:
    print("Du brauchst mindestens 8 Zeichen")
else:
    if not lower_check:
        print("Mindestens ein Kleinbuchstabe")
    if not upper_check:
        print("Mindestens ein Großbuchstabe")
    if not digit_check:
        print("Mindestens eine Zahl")
    if not symbol_check:
        print("Mindestens ein Sonderzeichen")
    if lower_check and upper_check and digit_check and symbol_check:
        print("Dein Passwort ist ausreichend sicher")









    
    # for character in password:
    #     if character.islower():
    #         lower_check = character.islower()
    #         break
    # for character in password:
    #     if character.isupper():
    #         upper_check = character.isupper()
    #         break
    # for character in password:
    #     if character.isdigit():
    #         digit_check = character.isdigit()
    #         break
    # for character in password:
    #     if character in symbol_list:
    #         symbol_check = True
    #         break

# if not lower_check:
#     print("Du brauchst mindestens einen Kleinbuchstaben")
# if not upper_check:
#     print("Du brauchst mindestens einen Großbuchstaben")
# if not digit_check:
#     print("Du brauchst mindestens eine Zahl")
# if not symbol_check:
#     print("Du brauchst mindestens ein Sonderzeichen (-,?,!,#)")


