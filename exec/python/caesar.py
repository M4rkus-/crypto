def encrypt_caesar(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            shift_char = chr((ord(char) + shift - 65) % 26 + 65)
            if char.islower():
                shift_char = shift_char.lower()
            ciphertext += shift_char
        else:
            ciphertext += char
    return ciphertext

plaintext = "Dies ist ein Beispieltext"
shift = 3
ciphertext = encrypt_caesar(plaintext, shift)
print("Originaltext:", plaintext)
print("Verschlüsselter Text:", ciphertext)
