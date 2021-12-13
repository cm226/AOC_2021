from types import SimpleNamespace

input = open("day13.dat", "r")
marks = []
folds = []

def doFold(axis, index):
    for mark in marks:
        if axis == 'y' and mark.y >= index:
            mark.y = index - (mark.y - index)
        if axis == 'x' and mark.x >= index:
            mark.x = index - (mark.x - index)

def printMarks():
    # find size of paper
    height = 0
    width = 0
    for mark in marks:
        if mark.x > width:
            width = mark.x
        if mark.y > height:
            height = mark.y
    

    grid = [[' ' for x in range(width+1)] for y in range(height+1)]
    for mark in marks:
        grid[mark.y][mark.x] = '*'

    for y in grid:
        print(''.join(y))


for line in input:
    line = line.strip()
    if(len(line)== 0):
        continue
    if 'fold' in line:
        useful = line[11:]
        (axis, index) = useful.split('=')
        folds.append((axis, int(index)))
    else:
        (xstr, ystr) = line.split(',')
        marks.append(SimpleNamespace(x=int(xstr), y=int(ystr)))

while len(folds) > 0:
    fold = folds.pop(0)
    doFold(fold[0], fold[1])

printMarks()