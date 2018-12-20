from operator import itemgetter

dir = {
	'N' : [0,-1],
	'E' : [1, 0],
	'W' : [-1,0],
	'S' : [0, 1]
}
cycles = [
	'NEWS', 'NESW', 'NSEW', 'SNEW', 'SNWE', 'SWNE', 'WSNE', 'WSEN', 'WESN', 'EWSN', 'EWNS', 'ENWS'
]
grid = {} #(x,y) -> (0: open space, 1: NS door, 2: WE door)

def get_input(f_path):
	input = open(f_path, 'r').read()
	finished = False
	
	while not finished:
		before = input
		for c in cycles:
			input = input.replace(c, '')
		if before == input:
			finished = True
	return list(input)

def branch_gen(ptr, input, dist):
	global grid
	start_ptr = ptr[:]
	start_dist = dist
	
	grid[(ptr[0],ptr[1])] = (0,dist)
	while len(input) > 0:
		char = input.pop(0)
		if char in ['N','W','E','S']:
			ptr[0] += dir[char][0]
			ptr[1] += dir[char][1]
			dist += 1
			if char in ['N','S']:
				if (ptr[0],ptr[1]) not in grid:
					grid[(ptr[0],ptr[1])] = (1,dist)
			else:
				if (ptr[0],ptr[1]) not in grid:
					grid[(ptr[0],ptr[1])] = (2,dist)
			ptr[0] += dir[char][0]
			ptr[1] += dir[char][1]
			if (ptr[0],ptr[1]) not in grid:
				grid[(ptr[0],ptr[1])] = (0,dist)
		elif char == '(':
			depth = 1
			sub_branch = []
			while depth != 0:
				char = input.pop(0)
				if char == '(':
					depth += 1
				elif char == ')':
					depth -= 1
				sub_branch.append(char)
			branch_gen(ptr, sub_branch, dist)
		elif char == '|':
			ptr = start_ptr
			dist = start_dist

def print_grid():
	out = open('out.txt', 'a')
	min_y = min(grid.keys(), key=itemgetter(1))[1] - 1
	min_x = min(grid.keys(), key=itemgetter(0))[0] - 1
	max_y = max(grid.keys(), key=itemgetter(1))[1] + 1
	max_x = max(grid.keys(), key=itemgetter(0))[0] + 1
	
	for y in range(min_y, max_y + 1):
		line = ''
		for x in range(min_x, max_x + 1):
			pt = (x,y)
			if pt == (0,0):
				line += 'X'
			elif pt in grid:
#				line += str(grid[pt][1]).zfill(2)
				if grid[pt][0] == 0:
					line += '.'
				elif grid[pt][0] == 1:
					line += '-'
				else:
					line += '|'
			else:
#				line += '##'
				line += '#'
		out.write(line+'\n')
		print(line)

def main():
	input = get_input('input.txt')
	branch_gen([0,0],input, 1)
	furthest_room = max(grid.items(), key=itemgetter(1))[1][1]
	far_rooms = 0
	for room in grid.values():
		if room[0] == 0 and room[1] >= 1000:
			far_rooms += 1
	
	print('furthest room is ',furthest_room,'doors away.')
	print('there are',far_rooms,'rooms at least 1000 doors away.')
main()