import os

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Schlüssel und IV aus Dateien lesen
with open("key.bin", "rb") as key_file, open("iv.bin", "rb") as iv_file:
    key = key_file.read()
    iv = iv_file.read()

# Abfrage ob verschlüsseln oder entschlüsseln ausgewählt wurde
mode = input("[E]ncrypt or [D]ecrypt? ").upper()

if mode == "E":
    # Text der verschlüsselt werden soll aus einer Datei lesen
    with open("plaintext.txt", "r") as plaintext_file:
        plaintext = plaintext_file.read()
    plaintext = plaintext.encode()

    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(plaintext)

    # Verschlüsselten Text in eine Datei schreiben
    with open("ciphertext.txt", "wb") as ciphertext_file:
        ciphertext_file.write(ciphertext)

    print("Text erfolgreich verschlüsselt.")

elif mode == "D":
    # Verschlüsselten Text aus einer Datei lesen
    with open("ciphertext.txt", "rb") as ciphertext_file:
        ciphertext = ciphertext_file.read()

    decipher = AES.new(key, AES.MODE_CBC, iv)
    deciphered_text = decipher.decrypt(ciphertext)

    # Entschlüsselten Text in eine Datei schreiben
    with open("deciphered_text.txt", "w") as deciphered_text_file:
        deciphered_text_file.write(deciphered_text.decode())

    print("Text erfolgreich entschlüsselt.")

else:
    print("Ungültige Eingabe.")
