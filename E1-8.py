# Write a Python program to encrypt a message using a Transposition cipher with double encryption.
import math

def transposition_encrypt(text, key):
    text = text.replace(" ", "")
    cols = len(key)
    rows = math.ceil(len(text)/cols)
    padded = text.ljust(rows*cols, 'X')
    grid = [padded[i:i+cols] for i in range(0, len(padded), cols)]
    order = sorted(range(cols), key=lambda k: key[k])
    result = ""
    for col in order:
        for row in grid:
            result += row[col]
    return result

# Input
msg = input("Enter message: ").upper()
key = input("Enter key: ").upper()

# Encrypt
once  = transposition_encrypt(msg, key)
twice = transposition_encrypt(once, key)

# Output
print("\nPlaintext         :", msg)
print("Single encryption :", once)
print("Double encryption :", twice)


# Enter message: MEET ME AFTER PARTY
# Enter key: ZEBRA

# Plaintext         : MEET ME AFTER PARTY
# Single encryption : METXEFAXEAPXTTRXMERY
# Double encryption : EARYTXTEEAXMXETRMFPX
