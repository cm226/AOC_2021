input = open("day11.dat", "r")

grid = []
count = 0

def onGrid(y,x):
    if x < 0 or y < 0:
        return False
    if y >= len(grid):
        return False
    if x >= len(grid[y]):
        return False
    return True


def doFlash(py, px):
    positions = []
    for y in range(-1,2):
        for x in range(-1,2):
            if not(x == 0 and y == 0):
                pos = (py+y, px+x)
                if onGrid(pos[0], pos[1]):
                    positions.append(pos)
    
    for pos in positions:
        grid[pos[0]][pos[1]] += 1


def step():
    global count
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            grid[y][x] +=1
    
    didFlash = True
    flashes = set()
    while(didFlash):
        didFlash = False
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] > 9 and (y,x) not in flashes:
                    doFlash(y, x)
                    count+=1
                    didFlash = True
                    flashes.add((y, x))
    
    if(len(flashes) == 100):
        return True

    for flash in flashes:
        grid[flash[0]][flash[1]] = 0

    return False

for line in input:
    line = line.strip()
    grid.append(list(map( lambda x : int(x), list(line))))


done = False
stepNo = 0
while not done:
    done = step()
    stepNo +=1

print(stepNo)