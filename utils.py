import random
def generateChineseRandomString():
    s=u''
    for i in range(random.randint(50, 100)):
        s=s+chr(random.randint(0x4E00, 0x9FA5))
    return s
