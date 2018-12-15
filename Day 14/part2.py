import os

scoreboard = [3,7]
elves = [0,1]
input = '440231' #<- puzzle input
target = []
for c in input:
	target.append(int(c))

while True:
	total = scoreboard[elves[0]] + scoreboard[elves[1]]
	if total > 9:
		scoreboard.append(1)
	scoreboard.append(total % 10)
	
	elves[0] = (elves[0] + scoreboard[elves[0]] + 1) % len(scoreboard)
	elves[1] = (elves[1] + scoreboard[elves[1]] + 1) % len(scoreboard)
	
	if len(scoreboard) > len(target):
		if scoreboard[-len(target):] == target:
			break
		if scoreboard[-len(target)-1:-1] == target:
			del scoreboard[-1]
			break

print('Appeared after', str(len(scoreboard)-len(target)))
