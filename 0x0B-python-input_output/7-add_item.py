#!/usr/bin/python3
"""script that adds all arguments to a Python list,
and then save them to a file:"""
import sys
import json


def main():
    lis = []
    for arg in sys.argv[1:]:
        lis.append(arg)
    try:
        with open("add_item.json", 'r') as f:
            old_list = json.load(f)
        new_list = old_list + lis

        with open("add_item.json", 'w') as f:
            json.dump(new_list, f)

    except FileNotFoundError:
        with open("add_item.json", 'w') as f:
            json.dump(lis, f)


if __name__ == "__main__":
    main()
