#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    le = []
    for i in range(list_length):
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
            le.append(dv)
    return length
