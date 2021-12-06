import functools
input = open("day6.dat", "r")

line = input.readline().split(',')
init = list(map(lambda x:int(x), line))

buckets = [0 for x in range(9)]

for f in init:
    buckets[f] += 1

for i in range(256):
    fishReady = buckets[0]
    for i in range(8):
        buckets[i] = buckets[i+1]
    buckets[8] = fishReady
    buckets[6] += fishReady
    
numFish = functools.reduce(lambda x, y: x+y, buckets)
print (numFish)
