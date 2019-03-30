#!/usr/bin/env python3

import sys
import re

def encodes(str, key):
    # declare return string
    ret = ""
    for character in str:
        # if there are any special characters, leave as is
        if re.match(r"[,\s\.~\!@#\$%\^&\*\(\)_\+{}\":;'\[\]]", character):
            ret = ret + character
            continue
        # get the corresponding number to the character
        temp = ord(character)
        temp += key
        # check and wrap if the new character went over the edge.
        if character.isupper():
            if temp > ord('Z'):
                temp -= 26
        elif character.islower():
            if temp > ord('z'):
                temp -= 26
        ret = ret + (chr(temp))

    print(ret)

def decodes(str, key):
    # declare return string
    ret = ""
    for character in str:
        # if there are any special characters, leave as is
        if re.match(r"[,\s\.~\!@#\$%\^&\*\(\)_\+{}\":;'\[\]]", character):
            ret = ret + character
            continue
        # get the corresponding number to the character
        temp = ord(character)
        temp -= key
        # check and wrap if the new character went over the edge.
        if character.isupper():
            if temp < ord('A'):
                temp += 26
        elif character.islower():
            if temp < ord('a'):
                temp += 26
        ret = ret + (chr(temp))

    print(ret)

if __name__ == '__main__':
    # Must have at least 3 arguements. Command Encode/Decode Key
    if len(sys.argv) < 3:
        print("Wrong number of arguments")
        print("Usage: ./cipher.py e/d key")
        print("e for encode. d for decode. Ceasar Key.")
        sys.exit()
    
    # Key must an integer
    if not sys.argv[2].isdigit():
        print("Invalid key. Must be an integer")
        sys.exit()

    decode = True
    key = int(sys.argv[2]) % 26
    if str.lower(sys.argv[1]) == 'e':
        decode = False
    elif str.lower(sys.argv[1]) == 'd':
        decode = True
    elif str.lower(sys.argv[1]) == 'h':
        print("Usage: ./cipher.py e/d key")
        print("e for encode. d for decode. key for how many characters to shift.")
    else:
        print("Invalid option. Program exiting")
        sys.exit()
    try:
        while True:
            message = input("Enter your message: ")
            message = str(message)
            if decode:
                decodes(message, key)
            else:
                encodes(message, key)
    except KeyboardInterrupt:
        print("\nGoodbye!\n")
