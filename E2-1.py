#	Write a Python program to encrypt and decrypt a message using DES.

from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

def encrypt(msg, key):
    key = key.encode()[:8].ljust(8, b' ')   # DES key = 8 byte
    cipher = DES.new(key, DES.MODE_ECB)
    ct = cipher.encrypt(pad(msg.encode(), 8))
    return ct

def decrypt(ct, key):
    key = key.encode()[:8].ljust(8, b' ')
    cipher = DES.new(key, DES.MODE_ECB)
    pt = unpad(cipher.decrypt(ct), 8)
    return pt.decode()

# Input
msg = input("Enter message: ")
key = input("Enter key (max 8 chars): ")

# Encrypt & Decrypt
cipher = encrypt(msg, key)
plain  = decrypt(cipher, key)

# Output
print("\nEncrypted (bytes):", cipher)
print("Decrypted:", plain)