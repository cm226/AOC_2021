from collections import namedtuple
import math

input = open('day15.dat', 'r')

graph = []
Point = namedtuple('Point', ['x', 'y'])

def getCost(pos):
    tileX = math.floor(pos.x/len(graph[0]))
    tileY = math.floor(pos.y/len(graph))
    x = pos.x % len(graph[0])
    y = pos.y % len(graph)
    cost = (graph[y][x] + tileY + tileX)
    if cost >9:
        cost -=9
    return cost

def getNeighbours(pos):
    n = []
    width = (len(graph[0])*5)-1
    height = (len(graph)*5)-1

    if pos.x > 0:
        n.append(Point(pos.x-1, pos.y))
    if pos.x < width:
        n.append(Point(pos.x+1, pos.y))
    if pos.y > 0:
        n.append(Point(pos.x, pos.y-1))
    if pos.y < height:
        n.append(Point(pos.x, pos.y+1))
    return n

for line in input: 
    graph.append(list(map(lambda x : int(x), list(line.strip()))))

# run dikjstra
start = Point(0,0)
end = Point((len(graph[0])*5)-1, (len(graph)*5)-1)

c = getCost(end)
neighbours = [start]
costs = {start : 0}

while len(neighbours) != 0:
    cur = neighbours.pop(0)
    if cur == end:
        break

    local = getNeighbours(cur)
    for next in local:
        cost = getCost(next)
        totalCost = costs[cur] + cost

        if next not in costs or totalCost < costs[next]:
            costs[next] = totalCost
            neighbours.append(next)
            neighbours.sort(key=lambda item: costs[item])

print(costs[end])
