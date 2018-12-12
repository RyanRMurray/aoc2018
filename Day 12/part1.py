import os

def print_seq(seq):
	line = ''
	for val in seq.values():
		if val:
			line += '#'
		else:
			line += '.'
	print(line)

#get sequence from input
sequence = {}
input = open('test2.txt', 'r')
index = 0
for char in input.readline().rstrip()[15:]:
	if char == '#':
		sequence[index] = True
	else:
		sequence[index] = False
	index += 1
	

#get rules from input
input.readline()

rules = {}
in_rule = input.readline().rstrip()
while in_rule:
	new_rule = []
	for ptr in range(5):
		if in_rule[ptr] == '#':
			new_rule.append(True)
		else:
			new_rule.append(False)
	
	if in_rule[-1] == '#':
		outcome = True
	else:
		outcome = False
	
	rules[tuple(new_rule)] = outcome
	in_rule = input.readline().rstrip()

input.close()
#impose rules on generation of plants
gens = 20
for gen in range(gens):
	left = min(sequence, key = int)
	right = max(sequence, key = int)
	new_seq = {}
	#for each point in range..
	for ptr in range(left - 2, right + 2):
		#impose each rule in turn, recording the result.
		comparison = []
		for pt in range(ptr-2,ptr+3):
			if pt in sequence:
				comparison.append(sequence[pt])
			else:
				comparison.append(False)
		if tuple(comparison) in rules:
			new_seq[ptr] = rules[tuple(comparison)]
		else:
			new_seq[ptr] = False
	
	#check edge cases, reducing graph to prevent massive memory inflation
	for ptr in range(left -2, left + 1):
		if new_seq[ptr]:
			break
		elif ptr == left:
			for pt in range(left - 2, left + 1):
				del new_seq[pt]
	
	for ptr in range(right, right + 2):
		if new_seq[ptr]:
			break
		elif ptr == right + 1:
			for pt in range(right, right + 2):
				del new_seq[pt]
	#displays an output similar to the example
	sequence = new_seq
	print_seq(sequence)

#get plant total thing idk
total = 0
for key, val in sequence.items():
	if val:
		total += key
		
print(total)





