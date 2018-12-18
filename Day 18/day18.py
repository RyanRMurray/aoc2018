grid = []
chars = {
	0 : '.',
	1 : '|',
	2 : '#',
	'.' : 0,
	'|' : 1,
	'#' : 2}

def get_input(f_path):
	global grid
	grid = []
	trees = 0
	yards = 0
	input = open(f_path, 'r')
	for line in input:
		line = line.rstrip()
		row = []
		for c in line:
			if c == '|':
				trees += 1
			elif c == '#':
				yards += 1
			row.append(chars[c])
		grid.append(row)
	return [trees, yards]

def print_grid():
	for row in grid:
		line = ''
		for c in row:
			line += chars[c]
		print(line)

def count(x, y, object):
	global grid
	count = 0
	if grid[y][x] == object:
		count -= 1
	for y_d in range(-1,2):
		for x_d in range(-1,2):
			if y + y_d in range(len(grid)) and x + x_d in range(len(grid[0])):
				if grid[y+y_d][x+x_d] == object:
					count += 1
	return count

def solve(limit):
	global grid
	input = get_input('input.txt')
	trees = input[0]
	yards = input[1]
	ticks = 0
	prev_grids = []
	prev_ticks = []
	prev_ptr = 0
#	print_grid()
#	print()
	while ticks < limit:
		#store in previously seen grids
		if len(prev_grids) < 50:
			prev_grids.append([c[:] for c in grid])
			prev_ticks.append(ticks)
		else:
			prev_grids[prev_ptr] = [c[:] for c in grid]
			prev_ticks[prev_ptr] = ticks
			if prev_ptr == 49:
				prev_ptr = 0
			else:
				prev_ptr += 1
		
		new_grid = [c[:] for c in grid]
		ticks += 1
		for y, row in enumerate(grid):
			for x, obj in enumerate(row):
				if obj == 0:
					if count(x,y,1) >= 3:
						new_grid[y][x] = 1
						trees += 1
				elif obj == 1:
					if count(x,y,2) >= 3:
						new_grid[y][x] = 2
						trees -= 1
						yards += 1
				elif obj == 2:
					if count(x,y,1) == 0 or count(x,y,2) == 0:
						new_grid[y][x] = 0
						yards -= 1
		grid = [c[:] for c in new_grid]
		
		if grid in prev_grids:
			if ((1000000000 - ticks) % (ticks - prev_ticks[prev_grids.index(grid)])) == 0:
				break
		
#		print_grid()
#		print()
	print('yards:',yards,'trees:',trees)
	print('outcome:', yards*trees)

def main():
	print('part 1:')
	solve(10)
	print('part 2:')
	solve(1000000000)

main()