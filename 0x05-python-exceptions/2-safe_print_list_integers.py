#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    h = 0
    for j in range(x):
        try:
            print("{:d}".format(my_list[j]), end="")
            h += 1
        except(ValueError, TypeError):
            continue
    print()
    return h
