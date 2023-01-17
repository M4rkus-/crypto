import random
import string

def generate_otp(length, count):
    # Erstellt eine Liste von zufälligen One-Time-Pads
    pads = []
    for i in range(count):
        pad = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        pads.append(pad)
    return pads

# Beispielaufruf
pads = generate_otp(16, 5)
print(pads)
