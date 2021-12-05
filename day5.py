input = open("day5.dat", "r")

def isBetween(t, p1, p2):
    b1 = t - p1
    b2 = t - p2
    if b1 >= 0 and b2 <= 0:
        return True
    if b1 <= 0 and b2 >= 0:
        return True
    return False

def isNotDiag(p1, p2):
    return p1[0] == p2[0] or p1[1] == p2[1]

vents = []

for line in input.readlines():
    (start, end) = line.split("->")
    start = start.strip()
    end = end.strip()

    (sx,sy) = start.split(',')
    (ex, ey) = end.split(',')

    vents.append(((int(sx),int(sy)), (int(ex), int(ey))))

size = 1000
grid = [[0 for x in range(size)] for y in range(size)]

for vent in vents:
    start = vent[0]
    end = vent[1]

    curx = start[0]
    cury = start[1]

    grid[curx][cury] += 1
    done = False
    while not done:
        dif = end[0] - curx
        if dif > 0:
            curx += 1
        elif dif < 0:
            curx -= 1

        dif = end[1] - cury
        if dif > 0:
            cury += 1
        elif dif < 0:
            cury -= 1

        grid[curx][cury] += 1
        done = curx == end[0] and cury == end[1]
    
overlapCount = 0
for x in range(size):
    for y in range(size):
        if grid[x][y] >=2:
            overlapCount+=1

print(overlapCount)
#print(isBetween(9, 0, 9))