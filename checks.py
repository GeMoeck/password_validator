def function_lowercase(password):
    for character in password:
        if character.islower():
            return True 
    return False    

def function_uppercase(password):
    for character in password:
        if character.isupper():
            return True
    return False

def function_digit(password):
    for character in password:
        if character.isdigit():
            return True
    return False

def function_symbol(password, symbol_list):
    for character in password:
        if character in symbol_list:
            return True
    return False

def function_minlength(password, length):
    return True if len(password) >= length else False
    # if len(password) < length:
    #     return False
    # else: 
    #     return True