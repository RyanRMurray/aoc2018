from operator import itemgetter

dir = {
	'N' : [0,-1],
	'E' : [1, 0],
	'W' : [-1,0],
	'S' : [0, 1]
}
grid = {} #point -> 0 for open space, 1 for door

def get_input(f_path):
	input = open(f_path, 'r').read()
	return list(input)

def build_branch(string, ptr):
	global grid
	root = ptr
	
	while len(string) > 0:
		char = string.pop(0)
		if char in 'NEWS':
			d = dir[char]
			door = (ptr[0]+d[0],ptr[1]+d[1])
			next = (door[0]+d[0],door[1]+d[1])
			grid[door] = 1
			grid[next] = 0
			ptr = next
		elif char == '|':
			ptr = root
		elif char == '(':
			depth = 1
			sub_branch = ''
			while depth > 0:
				char = string.pop(0)
				if char == '(':
					depth += 1
				elif char == ')':
					depth -= 1
				sub_branch += char
			build_branch(list(sub_branch[0:-1]), ptr)

def bfs(start):
	path_grid = {}
	to_visit = [start]
	path_grid[start] = (0,None)
	
	while len(to_visit) > 0:
		visiting = to_visit.pop(0)
		doors = path_grid[visiting][0]
		for d in dir.values():
			check_door = (visiting[0]+d[0],visiting[1]+d[1])
			next = (check_door[0]+d[0],check_door[1]+d[1])
			if check_door in grid and grid[check_door] == 1:
				if next in path_grid:
					if path_grid[next][0] > doors + 1:
						path_grid[next] = (doors + 1, visiting)
						to_visit.append(next)
				else:
					path_grid[next] = (doors + 1, visiting)
					to_visit.append(next)
	return(path_grid.values())

def main():
	global grid
	grid[(0,0)] = 0
	build_branch(get_input('input.txt')[1:-1], (0,0))
	distances = bfs((0,0))
	max_doors = max(distances, key=itemgetter(0))[0]
	far_doors = 0
	for d in distances:
		if d[0] > 999:
			far_doors += 1
	
	print('furthest room is',max_doors,'doors away.')
	print('there are',far_doors,'at least 1000 doors away.')

main()
