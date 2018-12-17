grid = {}
y_max = 0
x_max = 0
x_min = 999

def get_input(f_path):
	input = open(f_path, 'r')
	global y_max
	global x_max
	global x_min
	global grid
	for line in input:
		line = line.strip()
		if line[0] == 'x':
			x = int(line[2:line.find(',')])
			y_s = int(line[line.find('y')+2:line.find('.')])
			y_e = int(line[line.find('.')+2:])
			for y in range(y_s,y_e+1):
				grid[(x,y)] = 0
			if y_e > y_max:
				y_max = y_e
			if x < x_min:
				x_min = x
			if x > x_max:
				x_max = x
		else:
			y = int(line[2:line.find(',')])
			x_s = int(line[line.find('x')+2:line.find('.')])
			x_e = int(line[line.find('.')+2:])
			for x in range(x_s,x_e+1):
				grid[(x,y)] = 0
			if y > y_max:
				y_max = y
			if x_s < x_min:
				x_min = x_s
			if x_e > x_max:
				x_max = x_e

def print_grid():
	output = open('out.txt', 'a')
	for y in range(0, y_max):
		line = ''
		for x in range(x_min-1, x_max+1):
			if (x,y) in grid:
				c = grid[(x,y)]
				if c == 0:
					line += '#'
				elif c == 1:
					line += '|'
				else:
					line += '~'
			else:
				line += '.'
		output.write(line + '\n')

def find_opposite_wall(loc, dir):
	below = (loc[0], loc[1] + 1)
	next = (loc[0] + dir, loc[1])
	if below not in grid:
		return False
	if next in grid:
		if grid[next] in [0,2]:
			return True
	else:
		return find_opposite_wall(next, dir)

def place_water(l):
	loc = (l[0],l[1])
	left = (loc[0]-1,loc[1])
	right = (loc[0]+1,loc[1])
	below = (loc[0],loc[1]+1)
	#falling water at loc
	grid[loc] = 1
	#check if at max depth
	if l[1] > y_max:
		grid[loc] = 4
		return True
	#drop water further until max reached, or clay/settled water
	if below not in grid:
		if place_water(below):
			return True
	#if below is settled water or clay...
	if grid[below] in [0,2]:
		#check for two connected walls...
		if find_opposite_wall(loc, 1) and find_opposite_wall(loc,-1):
			#and set water as settled if that is the case
			grid[loc] = 2
		#continue pouring water left and right of no clay blocks it
		if left not in grid:
			place_water(left)
		if right not in grid:
			place_water(right)

def main():
	get_input('input.txt')
	place_water([500,1])
	
	water = 0
	for key, val in grid.items():
		if val in [1,2]:
			water += 1
	print(water)
	print_grid()

main()
