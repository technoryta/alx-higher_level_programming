#!/usr/bin/python3

for alphabet in range(97, 123):
    if chr(alphabet) is not 'e' or chr(alphabet) is not 'q':
        print("{}".format(chr(alphabet)), end="")
