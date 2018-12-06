import os
import operator

input = open('input.txt', 'r')
coords = []

for row in input:
    coords.append((int(row[:row.find(',')]),int(row[row.find(' ')+1:-1])))

input.close()

#create an empty grid
grid = []

for i in range(500):
    row = []
    for j in range(500):
        row.append(0)
    grid.append(row)

#populate grid cells with sum of manhattan distances to all coordinates
for y, row in enumerate(grid):
    for x, cell in enumerate(row):
        for coord in coords:
            manhattan = abs(coord[0] - x) + abs(coord[1] - y)
            row[x] += manhattan

print(grid)
#find number of cells meeting criteria
area = 0
for row in grid:
    for cell in row:
        if cell < 10000:
            area += 1

#print maximum area
print(area)
