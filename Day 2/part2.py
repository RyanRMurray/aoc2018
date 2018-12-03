import os
import string

strings = list()
found = False
input = open("input.txt", "r")


for line in input:
	strings.append(line.rstrip())

for firstStr in strings:
	for secondStr in strings:
		diff = 0
		list1 = list(firstStr)
		list2 = list(secondStr)
		i = 0
		for first, second in zip(list1, list2):
			if first != second:
				diff += 1
				pos = i
			i += 1
			
		if diff == 1:
			found = True
			out = firstStr
			break
	if found: break

print(out[:pos] + out[pos+1:])


