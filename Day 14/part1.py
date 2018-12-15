import os

scoreboard = [3,7]
elves = [0,1]
target = 440231 #<- puzzle input

while True:
	total = scoreboard[elves[0]] + scoreboard[elves[1]]
	if total > 9:
		scoreboard.append(1)
	scoreboard.append(total % 10)
	
	elves[0] = (elves[0] + scoreboard[elves[0]] + 1) % len(scoreboard)
	elves[1] = (elves[1] + scoreboard[elves[1]] + 1) % len(scoreboard)
	
	if len(scoreboard) > target + 10:
		break

ten_r = ''
for r in scoreboard[target:target+10]:
	ten_r += str(r)

print('First 10 after target: ', ten_r)