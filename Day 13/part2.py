import os
import copy
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
		self.inter = inter #defines intersection behaviour
		self.crashed = False

def print_track(grid, trains):
	out = open('out.txt','a')
	for y in range(len(grid)):
		line = ''
		for x in range(len(grid[y])):
			for t in trains:
				train = False
				if t.x == x and t.y == y and not t.crashed:
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

def move_train(rail, train):
	#track behaviour
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

def get_input():
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
		return [grid, trains]

def main() :
	input = get_input()
	grid = input[0]
	trains = input[1]
	print('Number of trains: ', len(trains))
	trains.sort(key = lambda l:(l.y, l.x))
	crashed = 0


	while crashed < len(trains) - 1:
		#ensure trains are considered left to right, top to bottom.
		trains.sort(key = lambda l:(l.y, l.x))
		
		for t in trains:
			if not t.crashed:
				#get the rail the train is on
				rail = grid[t.y][t.x]
				#first, move the train
				move_train(rail, t)
				#then see if it has collided with another train
				for other_t in trains:
					if t != other_t and not other_t.crashed:
						if t.x == other_t.x and t.y == other_t.y:
							print('Collision at ', t.x, t.y)
							t.crashed = True
							other_t.crashed = True
							crashed += 2
		#for bug testing:
		#print_track(grid, trains)

	for t in trains:
		if not t.crashed:
			print('Last train found at ', t.x, t.y)

main()

