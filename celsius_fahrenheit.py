#!/usr/bin/python3

def convert(x):
	return ((float(9) /  5) *  x + 32)

CelsiusList = [32.3, 27.5, 2.3, 11.1]
fahrenheitList = list (map(convert, CelsiusList))


print (CelsiusList)
print (fahrenheitList)

