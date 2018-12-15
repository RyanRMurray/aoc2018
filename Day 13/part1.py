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
		print(line)

#get tracks and trains from input
grid = []
trains = []
with open('input.txt', 'r') as input:
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

crashed = False
while not crashed:
	#print_track(grid,trains)
	for train in trains:
		rail = grid[train.y][train.x]
		if rail == r.NE: # \
			if train.facing == 0:
				train.facing = 3
			elif train.facing == 1:
				train.facing = 2
			elif train.facing == 2:
				train.facing = 1
			else:
				train.facing = 0
		elif rail == r.NW: # /
			if train.facing == 0:
				train.facing = 1
			elif train.facing == 1:
				train.facing = 0
			elif train.facing == 2:
				train.facing = 3
			else:
				train.facing = 2
		elif rail == r.CROSS:
			if train.inter == 0:
				if train.facing == 0:
					train.facing = 3
				else:
					train.facing -= 1
				train.inter += 1
			elif train.inter == 1:
				train.inter += 1
			else:
				if train.facing == 3:
					train.facing = 0
				else:
					train.facing += 1
				train.inter = 0
		train.x += direction[train.facing][0]
		train.y += direction[train.facing][1]
	#check for collisions
	col_check = {}
	for train in trains:
		if (train.x,train.y) in col_check:
			print('Collision at ', train.x, train.y)
			crashed = True
			break
		else:
			col_check[(train.x,train.y)] = 0



