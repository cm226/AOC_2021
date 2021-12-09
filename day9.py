import functools

def validPos(x, y, grid):
    if y < 0 or y >=len(grid):
        return False
    if x < 0 or x >=len(grid[y]):
        return False
    return True
def localLow(x, y, grid):
    val = grid[y][x]

    up = (x, y+1)
    down = (x, y-1)
    left = (x-1, y)
    right = (x+1, y)
    pos = [up, down, left, right]

    low = True
    for p in pos:
        if not validPos(p[0], p[1], grid):
            continue

        girdVal = grid[p[1]][p[0]]
        if girdVal <= val:
            low = False

    return low
def findBasinSize(x,y, grid, counted):
    val = grid[y][x]

    if val == 9:
        return 0
    
    size = 1
    counted[y][x] = True

    up = (x, y+1)
    down = (x, y-1)
    left = (x-1, y)
    right = (x+1, y)
    pos = [up, down, left, right]

    for p in pos:
        if not validPos(p[0], p[1], grid):
            continue
        
        if counted[p[1]][p[0]]:
            continue

        size += findBasinSize(p[0], p[1], grid, counted)
    
    return size


grid = []
input = open("day9.dat", "r")

for line in input:
    grid.append(list(map( lambda x : int(x), list(line.strip()))))


lows = []
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if localLow(x, y, grid):
            lows.append((x,y))

sizes = []
counted = [[False for x in range(len(grid[0]))] for y in range(len(grid))]
for low in lows:
    size = findBasinSize(low[0], low[1], grid, counted)
    sizes.append(size)

sizes.sort()

mult = functools.reduce(lambda x,y : x*y, sizes[-3:])
print(mult)

