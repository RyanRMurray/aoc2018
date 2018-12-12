import os

def print_seq(seq):
	line = ''
	for val in seq.values():
		if val:
			line += '#'
		else:
			line += '.'
	print line

#get sequence from input
sequence = {}
input = open('input.txt', 'r')
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
#impose rules on generation of plants. Also check to see if sequence has converged to a stable pattern
gens = 50000000000
converged = False
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
				
	
	new_left = min(new_seq, key = int)
	new_right = max(new_seq, key = int)
	#check for convergence left
	for key, val in new_seq.items():
		if key + 1 in sequence:
			if val != sequence[key + 1]:
				break
			elif key == new_right:
				converged = True
	#check for convergence right
	for key, val in new_seq.items():
		if key - 1 in sequence:
			if val != sequence[key - 1]:
				break
			elif key == new_right:
				converged = True
	
	#displays an output similar to the example
	#print_seq(sequence))
	#if converged, ensure pattern of values is shifted to the target generation
	sequence = new_seq
	if converged:
		shiftby = gens - gen - 1
		break

total = 0
#get plant total thing idk
for key, val in sequence.items():
	if val:
		total += key + shiftby
		
print(total)





