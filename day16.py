from functools import reduce
import math

class Buffer:
    def __init__(self, bytes):
        self.bytes = bytes
        self.offset = 0
        self.idx = 0
        self.count = 0

    def take(self, n):

        self.count+=n
        mask = 0xF
        mask = mask >> self.offset
        first = self.bytes[self.idx]
        first = first & mask
        if n < 4 - self.offset:
            first = first >> (4 - self.offset) - n
            if self.offset + n > 4:
                self.idx += 1
            
            self.offset = (self.offset + n)%4

            return first

        val = first
        taken = 4 - self.offset
        self.idx += 1
        self.offset = 0
        while taken < n:
            v = self.bytes[self.idx]

            if (n - taken) < 4:
                mask = 0xF
                mask = 0xF & (mask << (4-(n - taken)))
                self.offset += (n - taken)
                val = val << (n - taken)
                v = v&mask
                v = v >> 4-(n - taken)
                val += v
                taken += (n - taken)
            else:
                val = val << 4
                val += v
                self.idx +=1
                taken+=4
        return val

    def getCount(self):
        return self.count

def extractHeader(buffer):
    version = buffer.take(3)
    type = buffer.take(3)
    return (version , type)

def extractLiteral(buffer):
    more = buffer.take(1)
    literal = 0
    while more :
        literal = literal << 4
        literal+=buffer.take(4)
        more = buffer.take(1)

    literal = literal << 4
    literal+=buffer.take(4)
    return literal

def calcOp(type, packets):
    if type == 0:
        return reduce(lambda x,y : x+y, packets)
    if type == 1:
        return reduce(lambda x,y : x*y, packets)
    if type == 2:
        return min(packets)
    if type == 3:
        return max(packets)
    if type == 5:
        if packets[0] > packets[1]:
            return 1
        return 0
    if type == 6:
        if packets[0] < packets[1]:
            return 1
        return 0
    if type == 7:
        if packets[0] == packets[1]:
            return 1
        return 0

def extractOp(buffer, myType):
    lengthType = buffer.take(1)
    children = []
    if lengthType == 0:
        bits = buffer.take(15)
        startC = buffer.getCount()
        endC = startC + bits
        while buffer.getCount() < endC:
            version, type = extractHeader(buffer)
            if type != 4 : 
                children.append(extractOp(buffer, type))
            else:
                children.append(extractLiteral(buffer))
    else:
        numPackets = buffer.take(11)
        for i in range(numPackets):
            version, type = extractHeader(buffer)
            if type != 4 : 
                children.append(extractOp(buffer, type))
            else:
                children.append(extractLiteral(buffer))

    return calcOp(myType, children)

input = open('day16.dat', 'r')
msg = list(map(lambda x : int(x,16), list(input.readline().strip())))

buffer = Buffer(msg)

version, type = extractHeader(buffer)

if type != 4:
    print(extractOp(buffer, type))
else:
    l = extractLiteral(buffer)




