
#Caesar Cipher to encypt a message


def encrypt(text,shift):
    caesar = ' '
    for char in text:
        if(char==' '):
            caesar = caesar+char
        elif(char.isupper()):
            caesar = caesar+chr((ord(char)+shift-65)%26+65)
        else:
            caesar = caesar+chr((ord(char)+shift-97)%26+97)
    return caesar
            




message = input("Enter a message in order to encrypt it")
shift = int(input("Enter the shift:-"))
print("The encrypted message is",encrypt(message,shift))
