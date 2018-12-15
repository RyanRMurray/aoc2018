import os
import sys
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

#for tag in string.ascii_uppercase:
for tag in string.ascii_uppercase:
    pre = set()
    for dep in dependencies:
        if dep[1] == tag:
            pre.add(dep[0])
            del dep
    newNode = node(tag,pre)
    nodes.append(newNode)

#sort and add work times
nodes.sort(key = lambda x: x.tag)
i = 1
for n in nodes:
    n.execTime = 60 + i
    i += 1

workers = [None] * 5
completed = set()
t = -1

while len(completed) < 26:
    #work on tasks
    for w in range(len(workers)):
        if workers[w] is not None:
            workers[w].execTime -= 1
            if workers[w].execTime == 0:
                completed.add(workers[w].tag)
                workers[w] = None

    #find ready nodes if workers available
    for w in range(len(workers)):
        if workers[w] is None:
            for n in range(len(nodes)):
                if nodes[n].pre.issubset(completed):
                    workers[w] = nodes[n]
                    del nodes[n]
                    break

    #time step
    t += 1
    
print(t)
