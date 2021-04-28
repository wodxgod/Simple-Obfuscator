import base64
import random


def generateChineseRandomString():
    s=u''
    for i in range(random.randint(50, 100)):
        s=s+chr(random.randint(0x4E00, 0x9FA5))
    return s

def stringToHex(text=""):
    hex_result = ""
    for letter in text:
        hex_result += hex(ord(letter)).replace("0x", "\\x")
    return hex_result
