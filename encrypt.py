import os
import sys
from createMasks import createMasks

def encrypt(text, degree, startImage, newImage, imgLen, systemXernya, byte):

    textLen = len(text)
    
    if textLen >= imgLen * degree / byte - systemXernya:
        print("Too long text")
        return

    firstSystemByte = startImage.read(systemXernya)
    newImage.write(firstSystemByte)

    textMask, imgMask = createMasks(degree)

    # while True:
    for i in range(textLen):
        symbol = text[i]

        if not symbol:
            break

        # print("\nSymbol {0}, bin {1:b}".format(symbol, ord(symbol)))

        symbol = ord(symbol)

        for _ in range(0, byte, degree):
            imgByte = int.from_bytes(startImage.read(1), sys.byteorder) & imgMask
            bits = symbol & textMask
            bits >>= (byte - degree)

            # print("img {0}, bits {1:b}, num {1:d}".format(imgByte,bits))

            imgByte |= bits

            # print('ENCODED: ' + str(imgByte))
            # print('Writing ' + str(imgByte.to_bytes(1, sys.byteorder)))
            
            newImage.write(imgByte.to_bytes(1, sys.byteorder))
            symbol <<= degree

    newImage.write(startImage.read())

    startImage.close()
    newImage.close()
