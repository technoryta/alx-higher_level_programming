#!/usr/bin/python3
"""Writes string to a text"""



def read_file(filename="", text=""):
	"""function writes string to text"""
	with open(filename, 'w') as f:
		return f.write(text)
