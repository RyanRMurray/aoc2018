import os
import sys

input = open('input.txt', 'r')

pos = []
vel = []

for star in input:
    newPos = star[star.find('<')+1:star.find('>')]
    newVel = star[star.find('y=<')+3:-2]
    pos.append([
        int(newPos[:newPos.find(',')]),
        int(newPos[newPos.find(',')+1:])
        ])
    vel.append([
        int(newVel[:newVel.find(',')]),
        int(newVel[newVel.find(',')+1:])
        ])

input.close()
#number of frames to iterate through:
time = 10580
minX = 9999
minY = 9999
output = open('output.txt', 'a')

for frame in range(time):
    #find max and min
    smallestX = min([star[0] for star in pos])
    largestX = max([star[0] for star in pos])
    smallestY = min([star[1] for star in pos])
    largestY = max([star[1] for star in pos])
    spanX = largestX - smallestX
    spanY = largestY - smallestY

    if spanX < minX:
        minX = spanX
    if spanY < minY:
        minY = spanY

    #draw frames

    if frame > 10570:
        for y in range(smallestY,largestY+1):
            line = ''
            for x in range(smallestX,largestX+1):
                if [x,y] in pos:
                    line += '#'
                else:
                    line += '.'
            output.write(line)
            output.write('\n')
        output.write('FRAME: ' + str(frame))
        output.write('\n')

    #move stars
    for star in range(0, len(pos)):
        pos[star][0] += vel[star][0]
        pos[star][1] += vel[star][1]

output.close()

#Answers can be find in generated file output.txt.
