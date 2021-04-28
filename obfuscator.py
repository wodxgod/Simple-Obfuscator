import os
import base64

from colorama import Fore

from utils import *
from sys import argv

# configuration
OFFSET = 10
VARIABLE_NAME = generateChineseRandomString()


def obfuscate(content):
    b64_content = base64.b64encode(content.encode()).decode()
    index = 0
    code = ''
    for _ in range(int(len(b64_content) / OFFSET) + 1):
        _str = ''
        for char in b64_content[index:index + OFFSET]:
            byte = str(hex(ord(char)))[2:]
            if len(byte) < 2:
                byte = '0' + byte
            _str += '\\x' + str(byte)
        if _ == 0:
            code += f'{VARIABLE_NAME} = "{_str}"\n'
        else:
            code += f'{VARIABLE_NAME} += "{_str}"\n'
        index += OFFSET
    code += f'exec(__import__("\\x62\\x61\\x73\\x65\\x36\\x34").b64decode({VARIABLE_NAME}.encode("\\x75\\x74\\x66\\x2d\\x38")).decode("\\x75\\x74\\x66\\x2d\\x38"))'
    return code


def main():
    print('############################')
    print('#                          #')
    print('#    Simple Obfuscator     #')
    print('#  by wodx and JMRaichDev  #')
    print('#                          #')
    print('############################')

    try:
        if len(argv) == 2:
            path = argv[1]
            if not os.path.exists(path):
                print('[-] File not found')
                exit()

            if not os.path.isfile(path) or not path.endswith('.py'):
                print('[-] Invalid file')
                exit()

            with open(file=path, mode='r', encoding='utf-8', errors='ignore') as file:
                file_content = file.read()

            obfuscated_content = obfuscate(file_content)

            if os.path.exists(f'{path.split(".")[0]} (obfuscated).py'):
                backup = 0
                while os.path.exists(f'{path.split(".")[0]} (obfuscated) ~ {backup}.bkp'):
                    backup =+ 1
                os.rename(f'{path.split(".")[0]} (obfuscated).py', f'{path.split(".")[0]} (obfuscated) ~ {backup}.bkp')

            with open(file=f'{path.split(".")[0]} (obfuscated).py', encoding="utf-8", mode='w') as file:
                file.write(obfuscated_content)

            print('[+] Script has been obfuscated')
        else:
            print(f'Usage: py {argv[0]} <file>')
    except Exception as err:
        print(Fore.RED + str(err))


if __name__ == '__main__':
    main()
