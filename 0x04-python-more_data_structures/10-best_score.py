#!/usr/bin/python3


def best_score(a_dictionary):
    """Returns biggest key"""

    if a_dictionary is None:
        return None
    elif type(a_dictionary) is not dict:
        return None

    sorted_dict = sorted(a_dictionary.items(), 
            key=lambda x:x[1], reverse=True)

    return (sorted_dict[0][0])
