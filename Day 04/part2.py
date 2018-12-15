import os
import string
import operator
from datetime import datetime

#create and sort a list of events
input = open('input.txt', 'r')
schedule = []
guardMinuteSlept = {} #key/values of form (guard number, minute) = frequency

for line in input:
	time = datetime.strptime(line[1:line.find(']')] , '%Y-%m-%d %H:%M')
	event = line[line.find(']')+2:]
	schedule.append((time,event))

schedule = sorted(schedule, key = lambda x: x[0])

guardNum = 0
startSleep = 0
for event in schedule:
	char = event[1][0]
	if char == 'G':
		guardNum = int(event[1][7:event[1].find('b')-1])
	elif char == 'f':
		startSleep = event[0]
	elif char == 'w':
		#update guardMinuteSlept with how many times guard has slept at that minute
		for minute in range(startSleep.minute, event[0].minute):
			if (guardNum, minute) in guardMinuteSlept:
				guardMinuteSlept[(guardNum, minute)] += 1
			else:
				guardMinuteSlept[(guardNum, minute)] = 1

#get highest frequency of times slept by a guard on a particular minute
guardMinute = max(guardMinuteSlept.items(), key = operator.itemgetter(1))[0]

print(guardMinute[0] * guardMinute[1])