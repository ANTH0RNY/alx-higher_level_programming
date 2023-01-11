#!/usr/bin/python3
for i in range(99):
    if i % 10 > i // 10:
        if i > 1:
            print(', ', end='')
        print(f'{i:0>2}', end="")
