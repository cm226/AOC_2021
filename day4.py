
def readInput(input):
    boards = []
    curLine = input.readline()
    while curLine != '':
        board = []
        while(curLine != '\n' and curLine != ''):
            sepLine = curLine.split(' ')
            sepLine = list(filter(lambda x : len(x)>0, sepLine))
            board.append(list(map(lambda x : int(x),sepLine)))
            curLine = input.readline()
        curLine = input.readline()
        boards.append(board)
    return boards

def markBoard(board, marks, num):
    for x, row in enumerate(board):
        for y, v in enumerate(row):
            if v == num:
                marks[x][y] = True
            
def checkBoard(mark):
    for x, row in enumerate(mark):
        allrowSet = True
        allcolSet = True
        for y, v in enumerate(row):
            allrowSet = allrowSet and v
            allcolSet = allcolSet and mark[y][x]
        
        if allcolSet or allrowSet:
            return True

    return False

def getScore(board, mark):
    sum = 0
    for row, mrow in zip(board, mark):
        for v, m in zip(row, mrow):
           if not m:
               sum +=v
    return sum 


input = open("day4.dat", "r")
numbers = list(map(lambda x : int(x), input.readline().split(',')))
input.readline() # Skip empty
boards = readInput(input)

boardsize = (len(boards[0]), len(boards[0][0]))
marks = []
for board in boards:
    mark = [[False for x in range(boardsize[1])] for y in range(boardsize[0])] 
    marks.append(mark)



# Run game
score = 0
wonboards = [False for x in range(len(boards))]
for num in numbers:
    for i, (board, mark) in enumerate(zip(boards, marks)):
        markBoard(board,mark, num)
        if checkBoard(mark):
            wonboards[i] = True
            last = True
            for w in wonboards:
                last = last and w
            if last:
                score = getScore(board, mark) * num
                print(score)
                break
    if score != 0:
        break




 