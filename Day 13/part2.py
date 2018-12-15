import os
import operator
from enum import Enum

#directions of train - north, east, south, west
direction = [[0,-1],[1,0],[0,1],[-1,0]]

#directions of rails
class r(Enum):
	NONE = 0
	WE = 1 #horizontal
	NS = 2 #vertical
	NW = 3 #/
	NE = 4 #\
	CROSS = 5 #intersection

class train_obj:
	def __init__(self, x, y, facing, inter):
		self.x = x
		self.y = y
		self.facing = facing
		self.inter = inter

def print_track(grid, trains):
	out = open('out.txt','a')
	for y in range(len(grid)):
		line = ''
		for x in range(len(grid[y])):
			for t in trains:
				train = False
				if t.x == x and t.y == y:
					line += 't'
					train = True
					break
			if not train:
				if grid[y][x] == r.NONE:
					line += ' '
				elif grid[y][x] == r.WE:
					line += '-'
				elif grid[y][x] == r.NS:
					line += '|'
				elif grid[y][x] == r.NE:
					line += '\\'
				elif grid[y][x] == r.NW:
					line += '/'
				elif grid[y][x] == r.CROSS:
					line += '+'
		out.write(line + '\n')
	out.write('\n')
	out.close()

#get tracks and trains from input
grid = []
trains = []
with open('test.txt', 'r') as input:
	y = 0
	for line in input:
		row = []
		x = 0
		for char in line:
			#rails
			if char == ' ':
				row.append(r.NONE)
			elif char == '-':
				row.append(r.WE)
			elif char == '|':
				row.append(r.NS)
			elif char == '/':
				row.append(r.NW)
			elif char == '\\':
				row.append(r.NE)
			elif char == '+':
				row.append(r.CROSS)
			#trains
			elif char == '^':
				trains.append(train_obj(x,y,0,0))
				row.append(r.NS)
			elif char == '>':
				trains.append(train_obj(x,y,1,0))
				row.append(r.WE)
			elif char == 'v':
				trains.append(train_obj(x,y,2,0))
				row.append(r.NS)
			elif char == '<':
				trains.append(train_obj(x,y,3,0))
				row.append(r.WE)
			x += 1
		grid.append(row)
		y += 1

print('Number of trains: ', len(trains))
trains.sort(key = lambda l:(l.y, l.x))
#get current locations
positions = []
for t in trains:
	positions.append((t.x, t.y))
while True:
	print_track(grid, trains)
	trains.sort(key = lambda l:(l.y, l.x))
	t = 0
	while t < len(trains):
		rail = grid[trains[t].y][trains[t].x]
		#track behaviour
		if rail == r.NE: # \
			if trains[t].facing == 0:
				trains[t].facing = 3
			elif trains[t].facing == 1:
				trains[t].facing = 2
			elif trains[t].facing == 2:
				trains[t].facing = 1
			else:
				trains[t].facing = 0
		elif rail == r.NW: # /
			if trains[t].facing == 0:
				trains[t].facing = 1
			elif trains[t].facing == 1:
				trains[t].facing = 0
			elif trains[t].facing == 2:
				trains[t].facing = 3
			else:
				trains[t].facing = 2
		elif rail == r.CROSS:
			if trains[t].inter == 0:
				if trains[t].facing == 0:
					trains[t].facing = 3
				else:
					trains[t].facing -= 1
				trains[t].inter += 1
			elif trains[t].inter == 1:
				trains[t].inter += 1
			else:
				if trains[t].facing == 3:
					trains[t].facing = 0
				else:
					trains[t].facing += 1
				trains[t].inter = 0
		trains[t].x += direction[trains[t].facing][0]
		trains[t].y += direction[trains[t].facing][1]
		new_pos = (trains[t].x, trains[t].y)
		#check for collisions
		if new_pos in positions:
			other = positions.index(new_pos)
			del trains[t]
			del trains[other]
			del positions[t]
			del positions[other]
		else:
			print(positions)
			print(t)
			positions[t] = new_pos
			t += 1
	if len(trains) == 1:
		break
print('Last remaining train found at ', trains[0].x, trains[0].y)

