import os
import sys
from encrypt import encrypt
from decrypt import decrypt

def start():
    while True:
        choise = int(input("Enter number: 1 for encode, 2 for decode, 3 for quit\n"))

        if choise == 1:
            # text = str(input("Enter text to encode"))
            text = "Lab 3 seti i telecommunikacii" #29
            degree = int(input("Enter degree of encoding: 1 or 2 or 4 or 8: \n"))
            # text = open('text.txt', 'r')
            start = "start.bmp"
            new = "newImage.bmp"
            encrypt(text, degree, start, new, systemXernya=54, byte=8)

        elif choise == 2:
            degree = int(input("Enter degree of decoding: 1 or 2 or 4 or 8: \n"))
            toRead = int(input("How many symbols to read: \n"))
            new = "newImage.bmp"
            decrypt(degree, toRead, new, systemXernya=54, byte=8)

        elif choise == 3:
            break
        
        else:
            print("Unknown command!")

start()
