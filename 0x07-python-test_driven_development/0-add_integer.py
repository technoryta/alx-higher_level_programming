#!/usr/bin/python3
""" adds integers"""
def add_integer(a, b=98):
	"""adds two integers or floats
	
	Args:
		a: first integer
		b: second integer
	
	return:
		sum of a and b

	Raises:
		TypeError: if neither arguments are integer not float
	"""
	if not isinstance(a, int) and not isinstance(a, float):
		raise TypeError("a must be an integer")
	if not isinstance(b, int) and not isinstance (b, float):
		raise TypeError("b must be an integer")
	return (int(a) + int(b))
