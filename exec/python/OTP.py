#!/usr/bin/env python3

def encrypt_otp(plaintext, key):
    ciphertext = ""
    for i in range(len(plaintext)):
        ciphertext += chr(ord(plaintext[i]) ^ ord(key[i % len(key)]))
    return ciphertext

def decrypt_otp(ciphertext, key):
    plaintext = ""
    for i in range(len(ciphertext)):
        plaintext += chr(ord(ciphertext[i]) ^ ord(key[i % len(key)]))
    return plaintext

# Beispielnutzung
plaintext = "DIESISTEINBEISPIEL"
key = "SECRETKEY"
ciphertext = encrypt_otp(plaintext, key)
print("Verschlüsselter Text:", ciphertext)
decrypted_text = decrypt_otp(ciphertext, key)
print("Entschlüsselter Text:", decrypted_text)
