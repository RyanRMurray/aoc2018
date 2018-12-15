import os

grid = {}

input = open("input.txt","r")

for line in input:
	x = int(line[line.find('@')+2:line.find(',')])
	y = int(line[line.find(',')+1:line.find(':')])
	w = int(line[line.find(':')+2:line.find('x')])
	h = int(line[line.find('x')+1:])
	
	for i in range(w):
		for j in range(h):
			if (x+i,y+j) in grid:
				grid[(x+i,y+j)] += 1
			else:
				grid[(x+i,y+j)] = 1

input.close()
input = open("input.txt","r")

for line in input:
	overlap = False
	claim = line[:line.find('@')]
	x = int(line[line.find('@')+2:line.find(',')])
	y = int(line[line.find(',')+1:line.find(':')])
	w = int(line[line.find(':')+2:line.find('x')])
	h = int(line[line.find('x')+1:])
	
	for i in range(w):
		for j in range(h):
			if grid[(x+i,y+j)] > 1:
				overlap = True
				
	if not overlap:
		print(claim)
		break
