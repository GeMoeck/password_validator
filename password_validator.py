import string

password = input("Bitte Password eingeben: ")

length = len(password)

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
numbers = string.digits
symbols = string.punctuation
# requierements = [lowercase, uppercase, numbers, symbols]

lowercase_counter = 0
uppercase_counter = 0
numbers_counter = 0
symbols_counter = 0

if length < 8:
    print("Dein Passwort ist nicht lang genug. Du brauchst mindestens 8 Zeichen.")
else:
    for element in password:
        if element in lowercase:
            lowercase_counter += 1
        elif element in uppercase:
            uppercase_counter += 1
        elif element in numbers:
            numbers_counter += 1
        elif element in symbols:
            symbols_counter +=1
        else:
            print("In deinem Passwort sind nicht erlaubte Zeichen enthalten.")

if lowercase_counter == 0:
    print("Du brauchts mindestens einen Kleinbuchstaben")
if uppercase_counter == 0:
    print("Du brauchst mindestens einen Großbuchstaben")
if numbers_counter == 0:
    print("Du brauchst mindestens eine Zahl")
if symbols_counter == 0:
    print("Du brauchst mindestens ein Sonderzeichen")
