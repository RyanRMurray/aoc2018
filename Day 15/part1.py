import os

units = []
grid = []
directions = [[-1,0],[0,-1],[0,1],[1,0]] #NWES

class unit:
	def __init__(self, x, y, faction):
		self.hp = 200
		self.ap = 3
		self.x = x
		self.y = y
		self.faction = faction
		self.is_dead = False

def get_input():
	input = open('test.txt', 'r')
	
	y = 0
	for row in input:
		new_row = []
		x = 0
		for c in row.strip():
			if c == '.':
				new_row.append(True)
			elif c == 'E':
				units.append(unit(x, y, 0))
				new_row.append(True)
			elif c == 'G':
				units.append(unit(x, y, 1))
				new_row.append(True)
			else:
				new_row.append(False)
			x += 1
		grid.append(new_row)
		y += 1

def print_grid():
	y = 0
	for row in grid:
		x = 0
		line = ''
		for c in row:
			is_unit = False
			for u in units:
				if u.x == x and u.y == y and not u.is_dead:
					is_unit = True
					if u.faction == 0:
						line += 'E'
					else:
						line += 'G'
			if not is_unit:
				if c:
					line += '.'
				else:
					line += '#'
			x += 1
		y += 1
		print(line)

def get_next_move(u, locations):
	visited = {}
	visiting = [(u.x,u.y)]
	visited[(u.x,u.y)] = None
	target_found = False
	while len(visiting) > 0 and target_found == False:
		prev = visiting[0]
		#get adjacent squares in reading order
		for d in directions:
			next = (prev[0] + d[1], prev[1] + d[0])
			if next not in visited and grid[next[1]][next[0]]:
				#check for units here
				if next in locations:
					if locations[next].faction != u.faction:
						if not locations[next].is_dead:
							visited[next] = prev
							target_found = True
							target = next
							break
					else:
						continue
				#else add to queue
				visiting.append(next)
				visited[next] = prev
		visiting.pop(0)
	
	if not target_found:
		return None
	else:
		while visited[visited[target]] != None:
			target = visited[target]
		return target

def try_attack(u, locations):
	target = None
	for d in directions:
		adj = (u.x+d[1],u.y+d[0])
		if adj in locations:
			if locations[adj].faction != u.faction and not locations[adj].is_dead:
				#is valid enemy, compare with others
				if target == None or target.hp > locations[adj].hp:
					target = locations[adj]
	if target != None:
			print((u.x,u.y), 'attacks', (target.x,target.y))
			target.hp -= u.ap
			if target.hp < 1:
				target.is_dead = True
			return True
	return False

def main():
	get_input()
	fighting = True
	turn = -1
	
	while fighting:
		print_grid()
		#units have turns in reading order
		units.sort(key = lambda l:(l.y, l.x))
		#get initial locations and factions
		locations = {}
		for u in units:
			locations[(u.x,u.y)] = u
		
		for u in units:
			if not u.is_dead:
				#check for nearby enemies
				attacked = try_attack(u, locations)
				if not attacked:
					#check for valid moves
					next_move = get_next_move(u, locations)
					if next_move != None:
						print((u.x,u.y), 'to', next_move)
						del locations[u.x,u.y]
						#move to next location
						u.x = next_move[0]
						u.y = next_move[1]
						locations[(u.x,u.y)] = u
					
					try_attack(u, locations)
				#check if there are still enemies
				fighting = False
				for other_u in units:
					if other_u.faction != u.faction and not other_u.is_dead:
						fighting = True
		turn += 1
	print_grid()
	#outcome:
	hp_total = 0
	for u in units:
		if u.hp > 0:
			print(u.hp)
			hp_total += u.hp
	print(hp_total, turn)
	print(hp_total * turn)

main()