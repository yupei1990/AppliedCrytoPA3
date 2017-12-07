import random
import math


def rsaEncrypt(m, e, N, lenghN):
    lengthr = int(math.ceil(lenghN/2.0)) -2
    numberr = random.getrandbits(lengthr)
    stringr = bin(numberr)[2:]
    while lengthr != len(stringr):
        numberr = random.getrandbits(lengthr)
        stringr = bin(numberr)[2:]
    stringm = bin(m)[2:]
    if len(stringm) < lenghN/2:
        zeropadding = "0" * (lenghN/2 - len(stringm))
        stringm = zeropadding + stringm
    paddedMessage = stringr + stringm
    messageelement = int(paddedMessage, 2)
    return pow(messageelement, e, N)



rsaEncrypt()


