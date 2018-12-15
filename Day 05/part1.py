from itertools import filterfalse
import os

input = open('input.txt', 'r')
polymer = input.readline()
input.close()

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

print(len(polymer))