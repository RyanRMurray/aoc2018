import os

units = []
grid = [] #0: wall, 1: empty space, also contains goblins, elves
elf_num = 0
gob_num = 0
starting_elf_num = 0
directions = [[-1,0],[0,-1],[0,1],[1,0]] #NWES

class unit:
	def __init__(self, x, y, faction, ap):
		self.hp = 200
		self.ap = ap
		self.x = x
		self.y = y
		self.faction = faction
		self.is_dead = False

def get_input(elf_power): 
	input = open('input.txt', 'r')
	global elf_num
	global gob_num
	global starting_elf_num
	global units
	global grid
	gob_num = 0
	elf_num = 0
	starting_elf_num = 0
	units = []
	grid = []
	
	y = 0
	for row in input:
		new_row = []
		x = 0
		for c in row.strip():
			if c == '.':
				new_row.append(1)
			elif c == 'E':
				new_unit = unit(x, y, 2, elf_power)
				units.append(new_unit)
				new_row.append(new_unit)
				elf_num += 1
				starting_elf_num += 1
			elif c == 'G':
				new_unit = unit(x, y, 3, 3)
				units.append(new_unit)
				new_row.append(new_unit)
				gob_num += 1
			else:
				new_row.append(0)
			x += 1
		grid.append(new_row)
		y += 1
	input.close()

def print_grid():
	for row in grid:
		line = ''
		for c in row:
			if c == 0:
				line += '#'
			elif c == 1:
				line += '.'
			elif c.faction == 2 and not c.is_dead:
				line += 'E'
			elif not c.is_dead:
				line += 'G'
			else:
				line += 'X'
		print(line)

def try_move(u):
	distance_grid = {} #(distance from unit, preceding square)
	loc = (u.x,u.y)
	visiting = [loc]
	distance_grid[loc] = (0,None)
	target_spaces = []
	
	while len(visiting) > 0:
		prev = visiting.pop(0)
		prev_dist = distance_grid[prev][0]
		for d in directions:
			next = (prev[0] + d[1], prev[1] + d[0])
			if next not in distance_grid:
				in_space = grid[next[1]][next[0]]
				if in_space != 0:
					distance_grid[next] = (prev_dist+1, prev)
					#check if enemy
					if in_space != 1 and not in_space.is_dead:
						if in_space.faction != u.faction:
							target_spaces.append(next)
					else:
						visiting.append(next)
	#find closest target space
	if len(target_spaces) < 1:
		return None
	target_spaces.sort(key = lambda l:(l[1], l[0]))
	target = target_spaces[0]
	for t in target_spaces:
		if distance_grid[t][0] < distance_grid[target][0]:
			target = t
	#check if target is in reach
	if distance_grid[target][1] == loc:
		return None
	else:
		while distance_grid[target][1] != loc:
			target = distance_grid[target][1]
		return target

def try_attack(u):
	global elf_num
	global gob_num
	target = None
	
	for d in directions:
		adj = grid[u.y+d[0]][u.x+d[1]]
		if adj != 0 and adj != 1:
			if adj.faction != u.faction and not adj.is_dead:
				#is valid enemy, compare with others
				if target == None or target.hp > adj.hp:
					target = adj
	if target != None:
			#print((u.x,u.y), 'attacks', (target.x,target.y))
			target.hp -= u.ap
			if target.hp < 1:
				target.is_dead = True
				if target.faction == 2:
					elf_num -= 1
				else:
					gob_num -= 1
			return True
	return False

def battle():
	global starting_elf_num
	global elf_num
	global gob_num
	fighting = True
	turn = -1
	
	while fighting:
		#print_grid()
		turn += 1
		#units have turns in reading order
		units.sort(key = lambda l:(l.y, l.x))
		
		for u in units:
			if not u.is_dead and fighting == True:
				#check for nearby enemies
				attacked = try_attack(u)
				if not attacked:
					#check for valid moves
					next_move = try_move(u)
					if next_move != None:
						#print((u.x,u.y), 'to', next_move)
						#move to next location
						grid[u.y][u.x] = 1
						u.x = next_move[0]
						u.y = next_move[1]
						grid[u.y][u.x] = u
						try_attack(u)
				#check if there are still enemies
				if gob_num == 0 or elf_num == 0:
					fighting = False
	print_grid()
	#outcome:
	hp_total = 0
	for u in units:
		if u.hp > 0:
			hp_total += u.hp
	outcome = hp_total * turn
	
	if elf_num < starting_elf_num:
		return (False, outcome)
	else:
		return (True, outcome)

def main():
	elf_power = 4
	
	while True:
		get_input(elf_power)
		outcome = battle()
		if outcome[0]:
			print('Successful with power level', elf_power)
			print('Outcome:', outcome[1])
			break
		else:
			elf_power += 1

main()