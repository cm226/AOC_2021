from collections import namedtuple

def simSet(pos, dir, ammount):
        if(dir == 'forward'):
            return Position(pos.pos + ammount, pos.depth + (pos.aim * ammount), pos.aim )
        if(dir == 'down'):
            return Position(pos.pos, pos.depth, pos.aim + ammount)
        if(dir == 'up'):
            return Position(pos.pos, pos.depth, pos.aim - ammount)
        return pos

Position = namedtuple('Position', 'pos depth aim')

text_file = open("day2.dat", "r")
lines = text_file.readlines()

pos = Position(0,0, 0)
for line in lines:
    (dir, ammount) = line.split(" ")
    pos = simSet(pos, dir, int(ammount))

print(pos.pos * pos.depth)
