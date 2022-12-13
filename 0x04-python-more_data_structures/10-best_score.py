#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    sorted_list = (sorted(a_dictionary.items(), key=lambda x: x[1]))
    return (sorted_list[len(sorted_list) - 1][0])
