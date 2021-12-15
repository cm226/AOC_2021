import collections
input = open('day14.dat', 'r')

rules = {}
cache = {}

lines = input.readlines()

inputPol = list(lines[0].strip())

for rule in lines[2:]:
    start, end = rule.split(' -> ')
    rules[start.strip()] = end.strip()


def countPolymer(pairCount, elementCounts):
    newcount = collections.defaultdict(lambda :0)
    for pair in pairCount:
        between = rules[pair]
        elementCounts[between] += pairCount[pair]
        p1 = pair[0]+between
        p2 = between+pair[1]
        newcount[p1] += pairCount[pair]
        newcount[p2] += pairCount[pair]
    return (newcount, elementCounts)

pairCount = collections.defaultdict(lambda :0)
elementCounts = collections.defaultdict(lambda :0)

for i in range(len(inputPol)):
    elementCounts[inputPol[i]] += 1
    if i < len(inputPol)-1:
        pair = inputPol[i] + inputPol[i+1]
        pairCount[pair] +=1
    

for i in range(40):
    pairCount, elementCounts=countPolymer(pairCount, elementCounts)

elementCounts = sorted(elementCounts.items(), key=lambda item: item[1])
print(elementCounts[len(elementCounts)-1][1] - elementCounts[0][1])

