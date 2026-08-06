"""
BUILDING A CAESAR CIPHER

Challenge : Secret Message Encrypter & Decrypter

Create a python script that helps you send secret messages to your friend 
using simple encryption.

Your program should :
1. Ask the user if they want to (E)ncrypt or (D)ecrypt a message.
2. If Encrypting :
   - Ask for a message and numeric secret key.
   - Use a Caesar Cipher (shift letters by the key value).
   - Output the encrypted message.
3. If Decrypting :
   - Ask for the encrypted message and key.
   - Reverse the encryption to get the original message.

Rules :
- Only encrypt letters; leave spaces and punctuation as-is.
- Make sure the letters wrap around (e.g., 'z' + 1 -> 'a').

Bonus :
- Allow uppercase and lowercase letter handling.
- Show a clean interface.
"""

def encrypt(message, key):
    result = ""
    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + key) % 26 + base
            result += chr(shifted)
        else:
           result += char
    return result

def decrypt(message, key):
    return encrypt(message, -key)

print("Secret Message Program.")
choice = input("Do you want to E or D : ").strip().lower()

if choice == "e":
    text = input("Enter Your Encrypted Message : \n")
    try:
        key = int(input("Enter a number between 1 and 26 : "))
        encrypted = encrypt(text, key)
        print("Encrypted Message  : ")
        print(encrypted)
    except ValueError:
        print("Invalid key!")
elif choice == "d":
    text = input("Enter Your Decrypted Message : \n")
    try:
        key = int(input("Enter a number between 1 and 26 : "))
        decrypted = decrypt(text, key)
        print("Decrypted Message  : ")
        print(decrypted)
    except ValueError:
        print("Invalid key!")
else:
    print("Invalid Choice!")
