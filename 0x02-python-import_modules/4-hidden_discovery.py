#!/usr/bin/python3

import hidden_4

if __name__ == "__main__":
    all_names = dir(hidden_4)
    for name in all_names:
        if name[0] == '_' and name[1] == '_':
            continue
        print(name)
