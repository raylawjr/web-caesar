def alphabet_position(letter):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    char = letter.lower()
    for i in range(len(alphabet)):
        if char == alphabet[i]:
            return i

def rotate_character(char, rot):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(len(alphabet)):
        if char == alphabet[i]:
            return alphabet[(i+rot)%26]
        elif char == alphabet2[i]:
            return alphabet2[(i+rot)%26]
    return char

def encrypt(text, rot):
    newtext = ""
    for Char in text:
        newtext = newtext + rotate_character(Char, rot)
    return newtext
