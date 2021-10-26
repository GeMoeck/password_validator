password = input("Bitte Password eingeben: ")
symbol_list = ["-","?","!","#"]

lower_check = False
upper_check = False
digit_check = False
symbol_check = False

if len(password) < 8:
    print("Du brauchst mindestens 8 Zeichen")
else:
    for character in password:
        if character.islower():
            lower_check = character.islower()
            break
    for character in password:
        if character.isupper():
            upper_check = character.isupper()
            break
    for character in password:
        if character.isdigit():
            digit_check = character.isdigit()
            break
    for character in password:
        if character in symbol_list:
            symbol_check = True
            break

if not lower_check:
    print("Du brauchst mindestens einen Kleinbuchstaben")
if not upper_check:
    print("Du brauchst mindestens einen Großbuchstaben")
if not digit_check:
    print("Du brauchst mindestens eine Zahl")
if not symbol_check:
    print("Du brauchst mindestens ein Sonderzeichen (-,?,!,#)")