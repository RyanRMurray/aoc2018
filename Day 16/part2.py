import os

def get_samples():
	before = []
	code = []
	after = []
	input = open('input1.txt','r').readlines()
	
	for line in input:
		if len(line) > 1:
			if line[0] == 'B':
				i = line[line.find('[')+1:line.find(']')]
				before.append([int(x) for x in i.split(', ')])
			elif line[0] == 'A':
				i = line[line.find('[')+1:line.find(']')]
				after.append([int(x) for x in i.split(', ')])
			else:
				code.append([int(x) for x in line[:-1].split(' ')])
	
	return [before, code, after]

def get_program():
	codes = []
	input = open('input2.txt', 'r')
	for line in input:
		codes.append([int(x) for x in line.strip().split()])
	return codes

def addr(before, a, b, c):
	before[c] = before[a] + before[b]
	return before

def addi(before, a, b , c):
	before[c] = before[a] + b
	return before

def mulr(before, a, b, c):
	before[c] = before[a] * before[b]
	return before

def muli(before, a, b , c):
	before[c] = before[a] * b
	return before

def banr(before, a, b, c):
	before[c] = before[a] & before[b]
	return before

def bani(before, a, b , c):
	before[c] = before[a] & b
	return before

def borr(before, a, b, c):
	before[c] = before[a] | before[b]
	return before

def bori(before, a, b , c):
	before[c] = before[a] | b
	return before

def setr(before, a, b, c):
	before[c] = before[a]
	return before

def seti(before, a, b, c):
	before[c] = a
	return before

def gtir(before, a, b ,c):
	if a > before[b]:
		before[c] = 1
	else:
		before[c] = 0
	return before

def gtri(before, a, b ,c):
	if before[a] > b:
		before[c] = 1
	else:
		before[c] = 0
	return before

def gtrr(before, a, b, c):
	if before[a] > before[b]:
		before[c] = 1
	else:
		before[c] = 0
	return 0

def eqir(before, a, b, c):
	if a == before[b]:
		before[c] = 1
	else:
		before[c] = 0
	return before

def eqri(before, a, b, c):
	if before[a] == b:
		before[c] = 1
	else:
		before[c] = 0
	return before

def eqrr(before, a, b, c):
	if before[a] == before[b]:
		before[c] = 1
	else:
		before[c] = 0
	return before

ops = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]

def find_opcodes():
	input = get_samples()
	before = input[0]
	code = input[1]
	after = input[2]
	found_operations = [None] * 16
	
	for s in range(len(before)):
		compared = 0
		comparisons = [0] * 16
		for i, op in zip(range(16), ops):
			if after[s] == op(before[s].copy(), code[s][1], code[s][2], code[s][3]):
				comparisons[i] = 1
				compared += 1
		if compared == 1:
			found_operations[code[s][0]] = ops.pop(comparisons.index(1))
			continue
	#place left over instruction in unassigned number
	found_operations[found_operations.index(None)] = ops[0]
	return found_operations

def main():
	known_ops = find_opcodes()
	codes = get_program()
	reg = [0,0,0,0]
	for code in codes:
		known_ops[code[0]](reg, code[1], code[2], code[3])
	print(reg)

main()