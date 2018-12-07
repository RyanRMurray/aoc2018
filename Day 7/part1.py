import os
import string

class node:
    execTime = 0
    def __init__(self, tag, pre):
        self.tag = tag
        self.pre = pre

#generate list of tuples where (prerequisite step, step)
input = open('input.txt', 'r')
dependencies = []

for line in input:
    dependencies.append((line[5:6],line[36:37]))

#create ordered list of nodes
nodes = []
order = []

for tag in string.ascii_uppercase:
    pre = set()
    for dep in dependencies:
        if dep[1] == tag:
            pre.add(dep[0])
            dependencies.remove(dep)
    newNode = node(tag,pre)
    nodes.append(newNode)

nodes.sort(key = lambda x: x.tag)
#find next command that can be completed (alphabetically) and add it to the output string


while nodes:
    for n in nodes:
        found = True
        for p in n.pre:
            if p not in order:
                found = False
        if found == True:
            order.append(n.tag)
            nodes.remove(n)
            break

output = ''
for c in order:
    output += c

print(output)
