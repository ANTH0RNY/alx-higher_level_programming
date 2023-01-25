#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    length = []
    for i in range(list_range):
        try:
            dv = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            dv = 0
        except (ValueError, TypeError):
            print("wrong type")
            dv = 0
        except IndexError:
            print("out of range")
            dv = 0
        finally:
            length.append(dv)
    return length
