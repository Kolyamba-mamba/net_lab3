import os
import sys

def start():
    while True:
        choise = int(input("Enter number: 1 for encode, 2 for decode, 3 for quit\n"))

        if choise == 1:
            encrypt()
        elif choise == 2:
            decrypt()
        elif choise == 3:
            break
        else:
            print("Unknown command!")



def encrypt():
    # text = str(input("Enter text to encode"))
    text = "knowledge source"
    degree = int(input("Enter degree of encoding: 1 or 2 or 4 or 8: \n"))
    

    # textLen = os.stat('text.txt').st_size
    textLen = len(text)
    imgLen = os.stat('start.bmp').st_size
    system_xernya = 54
    if textLen >= imgLen * degree / 8 - system_xernya:
        print("Too long text")
        return

    # text = open('text.txt', 'r')
    startImage = open('start.bmp', 'rb')
    newImage = open('newImage.bmp', 'wb')  

    first54 = startImage.read(54)
    newImage.write(first54)

    textMask, imgMask = createMasks(degree)

    # while True:
    for i in range(textLen):
        symbol = text[i]

        if not symbol:
            break

        print("\nSymbol {0}, bin {1:b}".format(symbol, ord(symbol)))

        symbol = ord(symbol)

        for byteAmount in range(0, 8, degree):
            imgByte = int.from_bytes(startImage.read(1), sys.byteorder) & imgMask
            bits = symbol & textMask
            bits >>= (8 - degree)

            print("img {0}, bits {1:b}, num {1:d}".format(imgByte,bits))

            imgByte |= bits

            print('ENCODED: ' + str(imgByte))
            print('Writing ' + str(imgByte.to_bytes(1, sys.byteorder)))
            

            newImage.write(imgByte.to_bytes(1, sys.byteorder))
            symbol <<= degree

    # print(startImage.tell())

    newImage.write(startImage.read())

    startImage.close()
    newImage.close()


def decrypt():
    degree = int(input("Enter degree of decoding: 1 or 2 or 4 or 8: \n"))
    toRead = int(input("How many symbols to read: \n"))

    imgLen = os.stat('newImage.bmp').st_size

    if toRead >= imgLen * degree / 8 - 54:
        print("Too long read")
        return

    # text = open('decoded.txt', 'w')
    text = ""
    newImage = open('newImage.bmp', 'rb')

    newImage.seek(54)

    textMask, imgMask = createMasks(degree)
    imgMask = ~imgMask

    read = 0
    while read < toRead:
        symbol = 0

        for bitsRead in range(0, 8, degree):
            imgByte = int.from_bytes(newImage.read(1), sys.byteorder) & imgMask

            symbol <<= degree
            symbol |= imgByte

        # print("Symbol {0} is {1:c}".format(read, symbol))
        read += 1
        text += chr(symbol)
        # text.write(chr(symbol))
        
    print(text)

    # text.close()
    newImage.close()



def createMasks(degree):
    textMask = 0b11111111
    imgMask = 0b11111111

    textMask <<= (8 - degree)
    textMask %= 256 #костылик
    imgMask <<= degree

    return textMask, imgMask



start()
