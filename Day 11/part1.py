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

max = 0
powerGrid = []
coord = ()
for y in range(len(grid)-2):
    row = []
    for x in range(len(grid[0])-2):
        totalPower = 0
        for i in range(3):
            for j in range(3):
                totalPower += grid[x+i][y+j]
                if totalPower > max:
                    max = totalPower
                    coord = (y+1, x+1)
                    
        row.append(totalPower)



print(coord)
