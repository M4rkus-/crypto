#!/usr/bin/env python3

import random
import string

def generate_otp(length, count, file_name):
    # Erstellt eine Liste von zufälligen One-Time-Pads
    pads = []
    for i in range(count):
        pad = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        pads.append(pad)
    # Schreibt die Pads in eine Datei
    with open(file_name, 'w') as f:
        for pad in pads:
            f.write(pad + '\n')
    return pads

# Beispielaufruf
pads = generate_otp(16, 5, 'otp.txt')
print(pads)
