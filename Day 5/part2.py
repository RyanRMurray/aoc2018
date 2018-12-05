from itertools import filterfalse
import os
import string

input = open('input.txt', 'r')
originalPolymer = input.readline()
input.close()
lengths = []
print(len(originalPolymer))

for u in string.ascii_lowercase:
	polymer = originalPolymer
	polymer = polymer.replace(u, "")
	polymer = polymer.replace(u.upper(), "")
	changed = True
	
	while changed:
		changed = False
		i = 0
		newPolymer = ""
		while i < len(polymer)-1:
			unit = polymer[i]
			nextUnit = polymer[i+1]
			if (unit != nextUnit) and (unit.upper() == nextUnit.upper()):
				i += 1
				changed = True
			else:
				newPolymer += polymer[i]
			i += 1
		newPolymer += polymer[i]
		polymer = newPolymer
	lengths.append(len(polymer))

print(min(lengths))