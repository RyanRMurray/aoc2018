import os
from collections import deque, defaultdict

f = open('input.txt', 'r')
input = f.read()
f.close()

players = int(input[:input.find('p')])
lastMarbleVal = int(input[input.find('h ')+2:input.find(' points')]) * 100
#for testing:
#lastMarbleVal = 7999
#players = 13

scores = defaultdict(int)
circle = deque([0])
#refers to index of current marble in list circle
currentElfIndex = 0

for m in range(1,lastMarbleVal+1):
	
	if m % 23 == 0:
		#scoring turn
		circle.rotate(7)
		scores[m % players] += m + circle.pop()
		circle.rotate(-1)
	else:
		#regular turn
		circle.rotate(-1)
		circle.append(m)
	

print(max(scores.values()))