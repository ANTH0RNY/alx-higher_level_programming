#!/usr/bin/python3
def uppercase(str):
    out = ''
    for c in str:
        if ord(c) > 96 and ord(c) < 123:
            out += chr(ord(c) - 32)
        else:
            out += c
    print(out)
