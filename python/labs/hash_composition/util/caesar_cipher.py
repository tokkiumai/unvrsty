def caesar_cipher(text, key):
    r = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            r += chr((ord(char) + key - 65) % 26 + 65)
        else:
            r += chr((ord(char) + key - 97) % 26 + 97)
    return r
