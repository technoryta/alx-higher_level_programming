#!/usr/bin/python3
"""Script adds all argumnets to a Python list
and savs to file"""


import sys

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    members = load_from_json_file("add_item.json")
except FileNotFoundError:
    members = []
members.extend(sys.argv[1:])
save_to_json_file(members, "add_items.json")

