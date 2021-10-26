password = input("Bitte Password eingeben: ")
symbol_list = ["-","?","!","#","_"]

lower_check = False
upper_check = False
digit_check = False
symbol_check = False

def function_lowercase():
    for character in password:
        if character.islower():
            return True 
    return False    

def function_uppercase():
    for character in password:
        if character.isupper():
            return True
    return False

def function_digit():
    for character in password:
        if character.isdigit():
            return True
    return False

def function_symbol():
    for character in password:
        if character in symbol_list:
            return True
    return False

lower_check = function_lowercase()
upper_check = function_uppercase()
digit_check = function_digit()
symbol_check = function_symbol()

if len(password) < 8:
    print("Du brauchst mindestens 8 Zeichen")
else:
    if lower_check == False:
        print("Mindestens ein Kleinbuchstabe")
    if upper_check == False:
        print("Mindestens ein Großbuchstabe")
    if digit_check == False:
        print("Mindestens eine Zahl")
    if symbol_check == False:
        print("Mindestens ein Sonderzeichen")
    if lower_check == True and upper_check == True and digit_check == True and symbol_check ==True:
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


