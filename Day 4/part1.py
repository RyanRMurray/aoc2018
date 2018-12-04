import os
import string
import operator
from datetime import datetime

#create and sort a list of events
input = open('input.txt', 'r')
schedule = []
guardAsleep = {}

for line in input:
	time = datetime.strptime(line[1:line.find(']')] , '%Y-%m-%d %H:%M')
	event = line[line.find(']')+2:]
	schedule.append((time,event))

schedule = sorted(schedule, key = lambda x: x[0])

#dict guard number -> time spent asleep
guardNum = 0
startSleep = 0
for event in schedule:
	char = event[1][0]
	if char == 'G':
		guardNum = event[1][7:event[1].find('b')-1]
	elif char == 'f':
		startSleep = event[0]
	elif char == 'w':
		timeAsleep = event[0].minute - startSleep.minute
		if guardNum in guardAsleep:
			guardAsleep[guardNum] += (timeAsleep)
		else:
			guardAsleep[guardNum] = (timeAsleep)

#guard with most time asleep
target = max(guardAsleep.items(), key = operator.itemgetter(1))[0]

#get most frequent minute asleep
minutes = {}
targetGuard = False
startSleep = 0

for event in schedule:
	char = event[1][0]
	if char == 'G':
		guardNum = event[1][7:event[1].find('b')-1]
		if guardNum == target:
			targetGuard = True
			
	if targetGuard:
		if char == 'f':
			startSleep = event[0]
		elif char == 'w':
			for m in range(startSleep.minute, event[0].minute):
				if m in minutes:
					minutes[m] += 1
				else:
					minutes[m] = 1
			targetGuard = False

targetMinute = max(minutes.items(), key = operator.itemgetter(1))[0]

print(targetMinute * int(target))