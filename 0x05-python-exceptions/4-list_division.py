#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    divs = []
    for i in range(list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            div = 0
            print("division by 0")
            continue
        except TypeError:
            div = 0
            print("wrong type")
            continue
        except IndexError:
            div = 0
            print("out of range")
            continue
        finally:
            divs.append(div)
    return divs
