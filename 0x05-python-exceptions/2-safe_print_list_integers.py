#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Safely prints integers from a list"""

    try:
        printed = 0
        count = 0

        while count < x:
            try:
                print("{:d}".format(my_list[count]), end="")
                printed = printed + 1
                count = count + 1
            except (TypeError):
                conitne
            
            finally:
                print()
           
    except IndexError as e:
        raise
    finally:
        return printed
