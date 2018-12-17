import os

def get_input():
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

def main():
	input = get_input()
	before = input[0]
	code = input[1]
	after = input[2]
	mt_three_possible = 0

	for s in range(len(before)):
		compared = 0
		for op in ops:
			if after[s] == op(before[s][:], code[s][1], code[s][2], code[s][3]):
				compared += 1
		if compared > 2:
			mt_three_possible += 1

	print(mt_three_possible)

main()
