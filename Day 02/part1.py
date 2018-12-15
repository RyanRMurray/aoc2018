import os
import string

char_count = dict.fromkeys(string.ascii_lowercase, 0)
input = open("input.txt", "r")
twice = 0
thrice = 0

for line in input:
	for char in line:
		if char != "\n":
			char_count[char] += 1
		
	for count in char_count.values():
		if count == 2:
			twice += 1
			break
			
	for count in char_count.values():
		if count == 3:
			thrice += 1
			break
	char_count = dict.fromkeys(char_count.keys(), 0)

print(twice*thrice)