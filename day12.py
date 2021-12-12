class node :
    links = set()
    letter = ''

    def __init__(self, l):
        self.letter = l
        self.links = set()

    def addLink(self, node):
        self.links.add(node)
    
    def getLinks(self):
        return self.links
    
    def getletter(self):
        return self.letter

input = open("day12.dat", "r")

nodes = {}

def getOrCreateNode(letter):
    if letter not in nodes:
        nodes[letter] = node(letter)
        
    return nodes[letter]

def canDoubleBack(route):
    counts = {}
    for r in route:
        l = r.getletter()

        if l not in counts:
            counts[l] = 0

        counts[l] += 1
        if l.islower() and counts[l] >= 2:
            return False
    return True

def calcToVisit(route, node):
    links = node.getLinks()
    toVisit = []
    
    routeLinks = set()
    
    for r in route:
        letter = r.getletter()
        routeLinks.add(letter)
        

    for l in links:
        letter = l.getletter()
        if letter.islower() and letter in routeLinks:
            # if the route dosnt have any other revosoted small then we are good
            if letter == 'start' or letter == 'end':
                continue

            if not canDoubleBack(route):
                continue

        toVisit.append(l)
        
    return toVisit

            


def dfs(route):
    last = route[-1]
    tovisit = calcToVisit(route, last)

    if last == nodes['end']:
        return [route]
    
    if len(tovisit) == 0:
        return []

    newRoutes = []
    for v in tovisit:
        newroute = route.copy()
        newroute.append(v)
        newRoutes = newRoutes + dfs(newroute)
    
    return newRoutes
            



for line in input:
    line = line.strip()
    (start, end) = line.split('-')

    startNode = getOrCreateNode(start)
    endNode = getOrCreateNode(end)

    startNode.addLink(endNode)
    endNode.addLink(startNode)

route = [nodes['start']]
routes = dfs(route)

for r in routes:
    string = ''
    for n in r:
        string += n.getletter()+','
            
    print(string)
print(len(routes))
