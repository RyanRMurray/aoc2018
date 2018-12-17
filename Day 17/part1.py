import os

grid = {} #dict of (x,y) => clay 1/falling water 2/settled water 3
final = {}
y_min = 0
y_max = 0
x_min = 99999
x_max = 0

def get_input(f_path):
    global grid
    global x_min
    global x_max
    global y_max
    input = open(f_path, 'r')

    for line in input:
        line = line.strip()
        if line[0] == 'x':
            x = int(line[2:line.find(',')])
            y = int(line[line.find('y')+2:line.find('.')])
            y_e = int(line[line.find('.')+2:])
            if x < x_min:
                x_min = x - 1
            if x > x_max:
                x_max = x + 1
            while y < y_e + 1:
                grid[(x,y)] = 1
                y += 1
            if y > y_max:
                y_max = y - 1
        else:
            y = int(line[2:line.find(',')])
            x = int(line[line.find('x')+2:line.find('.')])
            x_e = int(line[line.find('.')+2:])
            if y > y_max:
                y_max = y - 1
            if x < x_min:
                x_min = x - 1
            while x < x_e + 1:
                grid[(x,y)] = 1
                x += 1
            if x > x_max:
                x_max = x + 1
    input.close()

def print_grid():
    for y in range(y_min, y_max+ 1):
        line = ''
        for x in range(x_min, x_max + 1):
            if (x,y) in grid:
                c = grid[(x,y)]
                if c == 1:
                    line += '#'
                elif c == 2:
                    line += '|'
                else:
                    line += '~'
            else:
                line += '.'
        print(line)

def try_settle(s):
    settling = True
    left = (s[0] - 1, s[1])
    right = (s[0] + 1, s[1])
    falling = False
    changed = [(s[0],s[1])]
    if (left in grid and right in grid) and (grid[left] in [2,3] or grid[right] in [2,3]):
        return [False, False]
    while settling:
        settling = False
        #check left
        if left not in grid:
            changed.append(left)
            if (left[0], left[1] + 1) not in grid:
                grid[left] = 2
                falling = True
            else:
                grid[left] = 3
                settling = True
        left = (left[0] - 1, left[1])
        #check right
        if right not in grid:
            changed.append(right)
            if (right[0], right[1] + 1) not in grid:
                grid[right] = 2
                falling = True
            else:
                grid[right] = 3
                settling = True
                right = (right[0] + 1, right[1])
    if falling:
        grid[(s[0],s[1])] = 2
        for c in changed:
            grid[(c[0],c[1])] = 2
    return [True, falling]

def main():
    get_input('input.txt')
    print_grid()
    running = True
    #initial waterfall
    grid[500, 1] = 2
    ticks = 0
    while running:
        ticks += 1
        running = False
        #check for falling waterfalls, settled water
        settled = []
        waterfalls = []
        filling = []
        for key, val in grid.items():
            if val == 2:
                waterfalls.append([key[0], key[1]])
            elif val == 3 and key not in final:
                settled.append([key[0], key[1]])
        #simulate waterfalls
        for w in waterfalls:
            below = (w[0],w[1]+1)
            left = (w[0]-1,w[1])
            right = (w[0]+1,w[1])
            falling = True
            while True and (w[0],w[1]) not in final:
                if below in grid:
                    if grid[below] == 1:
                        grid[(w[0],w[1])] = 3
                        running = True
                    elif grid[below] == 3:
                        filling.append(w)
                        final[(w[0],w[1])] = True
                    break
                elif below[1] <= y_max:
                    grid[below] = 2
                    w[1] += 1
                    running = True
                else:
                    falling = False
                    break
        #simulate settled water
        for s in settled:
            if try_settle(s)[0]:
                running = True
                final[(s[0],s[1])] = True
        #simulate water fill
        for f in filling:
            res = try_settle(f)
            if res[0] and not res[1]:
                grid[(f[0],f[1])] = 3
                running = True
            if res[0] and res[1]:
                grid[(f[0],f[1])] = 2
                running = True
        print(ticks)
    wet = 0
    for key, val in grid.items():
        if val == 2 or val == 3:
            wet += 1
    print(wet)


main()
