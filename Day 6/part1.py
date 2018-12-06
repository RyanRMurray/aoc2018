import os
import operator

class grid_cell:
        def __init__(self, distance = 0, coord = 0):
            self.distance = distance
            self.coord = coord

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
        cell = grid_cell(999999, 0)
        row.append(cell)
    grid.append(row)

#populate grid. each cell has a distance to and a closest coordinate
for y, row in enumerate(grid):
    for x, cell in enumerate(row):
        for c, coord in enumerate(coords):
            manhattan = abs(coord[0] - x) + abs(coord[1] - y)
            if manhattan == cell.distance:
                cell.coord = 0
            elif manhattan < cell.distance:
                cell.distance = manhattan
                cell.coord = c + 1

#add all coords closest to the edge to a blacklist, as they will be infinite
blacklist = set()

for cell in grid[0]:
    blacklist.add(cell.coord)

for row in grid:
    blacklist.add(row[0].coord)
    blacklist.add(row[-1].coord)

for cell in grid[-1]:
    blacklist.add(cell.coord)

#find area of each Coordinate
areas = {}
for row in grid:
    for cell in row:
        if cell.coord not in blacklist:
            if cell.coord in areas:
                areas[cell.coord] += 1
            else:
                areas[cell.coord] = 1

#print maximum area
print(max(areas.items(), key = operator.itemgetter(1))[1])
