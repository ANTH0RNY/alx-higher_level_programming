#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv, exit
    len = len(argv)
    if len - 1 == 1:
        print(f"{len - 1:d} argument")
    else:
        print(f"{len - 1:d} arguments")
    if not (len - 1):
        exit()
    for i in range(1, len):
        print(f"{i:d}: {argv[i]}")
