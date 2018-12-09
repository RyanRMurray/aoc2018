import os

f = open('input.txt', 'r')
input = f.read()
input = [int(i) for i in input.split()]
f.close()

total = 0
nodes = []

while 1:
	#recursively add starting from leaf
	while len(nodes) != 0 and nodes[-1][0] == 0:
		#sum of metadata
		total += sum(input[:nodes[-1][1]])
		#delete metadata values from list
		input = input[nodes[-1][1]:]
		nodes.pop()
	
	#check if all nodes processed
	if len(input) == 0:
		break
	
	#get next node
	cNum = input.pop(0)
	mNum = input.pop(0)
	
	#move through child nodes
	if len(nodes) > 0:
		nodes[-1][0] -= 1
	
	nodes.append([cNum, mNum])

print(total)