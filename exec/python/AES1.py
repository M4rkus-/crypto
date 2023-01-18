import os
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding

def encrypt(file_name):
    key = Fernet.generate_key()
    cipher = Fernet(key)

    # Reading plaintext from file
    with open(file_name, 'rb') as file:
        plaintext = file.read()

    # Encrypting the plaintext
    ciphertext = cipher.encrypt(plaintext)

    # Writing the ciphertext to file
    with open(file_name+'.encrypted', 'wb') as file:
        file.write(ciphertext)

    # Writing the key to a file
    with open('key.key', 'wb') as file:
        file.write(key)
        
def decrypt(file_name):
    # Reading the key from file
    with open('key.key', 'rb') as file:
        key = file.read()

    cipher = Fernet(key)

    # Reading ciphertext from file
    with open(file_name, 'rb') as file:
        ciphertext = file.read()

    # Decrypting the ciphertext
    plaintext = cipher.decrypt(ciphertext)

    # Writing the plaintext to file
    with open(file_name+'.decrypted', 'wb') as file:
        file.write(plaintext)
