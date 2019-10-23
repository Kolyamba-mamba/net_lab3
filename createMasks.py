
def createMasks(degree):
    textMask = 0b11111111
    imgMask = 0b11111111

    textMask <<= (8 - degree)
    textMask %= 256 #костылик
    imgMask <<= degree

    return textMask, imgMask