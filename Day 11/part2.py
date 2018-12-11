#NOTE:
#The following is not a general solution. It assumes the answer is a square less
#than 50 units across. It also takes a while to run. 

import os
input = 5719

grid = []
for y in range(1,301):
    row = []
    for x in range(1,301):
        first = (((x + 10) * y) + input) * (x + 10)
        second = int(str(first)[-3])
        power = second - 5
        row.append(power)
    grid.append(row)

maxPower = 0
coord = ()
for y in range(len(grid)-2):
    for x in range(len(grid[0])-2):
        print('Checking' + str((y+1,x+1)))
        limit = max(x, y, 250)
        for size in range(1, 297 - limit):
            totalPower = 0
            for i in range(size):
                for j in range(size):
                    totalPower += grid[x+i][y+j]
            if totalPower > maxPower:
                maxPower = totalPower
                coord = (y+1, x+1,size)
                print(coord)


print(coord)
