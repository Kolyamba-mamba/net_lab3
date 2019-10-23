import os
import sys
from createMasks import createMasks

def decrypt(degree, toRead, new, systemXernya, byte):

    newImage = open(new, 'rb')
    imgLen = os.stat(new).st_size

    if toRead >= imgLen * degree / byte - systemXernya:
        print("Too long read")
        return

    # text = open('decoded.txt', 'w')
    text = ""

    newImage.seek(systemXernya)

    _, imgMask = createMasks(degree)
    imgMask = ~imgMask

    read = 0
    while read < toRead:
        symbol = 0

        for _ in range(0, byte, degree):
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