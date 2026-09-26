#write a Python program to encrypt and decrypt a message using Caesar cipher.
def caesar_encrypt(text, shift):
    result = ""
    for c in text:
        if c.isalpha():
            base = 65 if c.isupper() else 97
            result += chr((ord(c) - base + shift) % 26 + base)
        else:
            result += c
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


plain_text = input("Enter Plain Text: ")
shift = int(input("Enter Shift Value: "))

cipher_text = caesar_encrypt(plain_text, shift)
decrypted = caesar_decrypt(cipher_text, shift)
print("Plain Text:", plain_text)
print("Cipher Text:", cipher_text)
print("Decrypted Text:", decrypted)



# message = "HELLO"
# shift   = 3