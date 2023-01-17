#!/usr/bin/env python3

import socket
import struct

def generate_otp(length, count, file_name):
    pads = []
    for i in range(count):
        pad = ""
        for j in range(length):
            # Erstellen eines UDP-Sockets
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            # Binden des Sockets an einen Port
            sock.bind(("", 0))
            # Senden einer Datagram-Anforderung
            sock.sendto(b"", ("8.8.8.8", 80))
            # Empfangen einer Antwort
            _, timestamp = sock.recvfrom(1024)
            # Wandelt das timestamp in einen long long integer
            timestamp = struct.unpack("!Q", timestamp)[0]
            # Fügt den timestamp dem Pad hinzu
            pad += str(timestamp)
        pads.append(pad)
    with open(file_name, 'w') as f:
        for pad in pads:
            f.write(pad + '\n')
    return pads

# Beispielaufruf
length = 20
count = 5
file_name = "otp.txt"
pads = generate_otp(length, count, file_name)
print(pads)
