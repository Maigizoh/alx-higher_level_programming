#!/usr/bin/python3
# Author - Bamidele Adefolaju

def magic_calculations(a, b, c):
    """match bytecode provided by Holberton School."""
    if a < b:
        return (c)
    if c < b:
        return (a + b)
    return (a*b - c)
