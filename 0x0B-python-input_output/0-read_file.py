#!/usr/bin/python3
"""A function that read text file UTF8"""


def read_file(filename=""):
	"""function reads and prints to stdout)"""
	with open(filename) as f:
		myfile = f.read()
		print(myfile, end="")
