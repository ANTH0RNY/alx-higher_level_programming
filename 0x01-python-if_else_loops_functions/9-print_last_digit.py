#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        lst = (abs(number) % 10) * -1
    else:
        lst = number % 10
    print(lst, end='')
    return lst
