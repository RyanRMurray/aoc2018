grid = {}
y_max = 0

def get_input(f_path):
    input = open(f_path, 'r')
    global y_max
    global grid

    for line in input:
        line = line.strip()
        if line[0] == 'x':
            x = int(line[2:line.find(',')])
            y_s = int(line[line.find('y')+2:line.find('.')])
            y_e = int(line[line.find('.')+2:])
            for y in range(y_s,y_e+1):
                grid[(x,y)] = 0
            if y_e > y_max:
                y_max = y_e
        else:
            y = int(line[2:line.find(',')])
            x_s = int(line[line.find('x')+2:line.find('.')])
            x_e = int(line[line.find('.')+2:])
            for x in range(x_s,x_e+1):
                grid[(x,y)] = 0
            if y > y_max:
                y_max = y

def print_grid():
    for y in range(0, y_max+ 1):
        line = ''
        for x in range(494, 505):
            if (x,y) in grid:
                c = grid[(x,y)]
                if c == 0:
                    line += '#'
                elif c == 1:
                    line += '|'
                else:
                    line += '~'
            else:
                line += '.'
        print(line)

def place_water(l):
    loc = (l[0],l[1])
    left = (loc[0]-1,loc[1])
    right = (loc[0]+1,loc[1])
    below = (loc[0],loc[1]+1)
    above = (loc[0],loc[1]-1)
    #falling water at loc
    grid[loc] = 1
    print(loc)
    print_grid()
    if l[1] > y_max:
        grid[loc] = 4
        return
    if below not in grid:
        place_water(below)
    if grid[below] in [0,2]:
        if left in grid and grid[left] in [0,2]:
            grid[loc] = 2
        else:
            place_water(left)
        if right in grid and grid[right] in [0,2]:
                grid[loc] = 2
        else:
            place_water(right)


def main():
    get_input('test.txt')
    place_water([500,1])
    print_grid()

main()
