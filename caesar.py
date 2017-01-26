def alphabet_position(letter):
    """receive a letter and returns numerical position of that letter within the alphabet"""
    value = ord(letter.upper()) - 65
    return value

def rotate_character(char, rot):
    """receives a character and rotation amount, returns a new character after rotating it to the right"""
    newchar = ""
    if char.isalpha() == False:
        newchar = char
        return newchar
    elif char.islower():
        newchar = ((alphabet_position(char) + rot) % 26) + 97
    else:
        newchar = ((alphabet_position(char) + rot) % 26) + 65
    newchar = chr(newchar)
    return newchar

def encrypt(text, rot):
    """ input text and rotation amount, return encrypted message"""
    rotatedword = ""
    for char in text:
        rotatedword = rotatedword + rotate_character(char, rot)
    return rotatedword
