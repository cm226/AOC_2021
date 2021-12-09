import functools

input = open("day8.dat", "r")

decode = {}

possibleVals = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
mappings = {
    'a' : ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
    'b' : ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
    'c' : ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
    'd' : ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
    'e' : ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
    'f' : ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
    'g' : ['a', 'b', 'c', 'd', 'e', 'f', 'g']
}
def sortKey(key):
    l = list(key)
    l.sort()
    return ''.join(l)

def fromMapping(str):
    str = sortKey(str.strip())
    mapped = []
    for c in str:
        mapped.append(mappings[c][0])

    mapped.sort()
    return ''.join(mapped)
def toNumber(str):
    str = sortKey(str.strip())

    if(str == fromMapping('cf')): #1
        return 1
    elif(str == fromMapping('acdeg')): #2
        return 2
    elif(str == fromMapping('acdfg')): #3
        return 3
    elif(str == fromMapping('bcdf')): #4
        return 4
    elif(str == fromMapping('abdfg')): #5
        return 5
    elif(str == fromMapping('abdefg')): #6
        return 6
    elif(str == fromMapping('acf')): #7
        return 7
    elif(str ==fromMapping('abcdefg')): #8
        return 8
    elif(str == fromMapping('abcdfg')): #9
        return 9
    elif(str == fromMapping('abcefg')): #0
        return 0

def toSet(key):
    return set(list(key.strip()))

def reduce(mappings):
    for i in range(2):
        for mapping in mappings:
            if len(mappings[mapping]) == 1:
                for m in mappings:
                    if len(mappings[m]) != 1 and mappings[mapping][0] in mappings[m]:
                        mappings[m].remove(mappings[mapping][0])
def deduceOne(digit):
    if len(digit) == 2:
        decode[sortKey(digit)] = 1
        rdecode[1] = sortKey(digit)
        list_difference = [item for item in possibleVals if item not in list(digit)]
        for c in list_difference:
            if c in mappings['c']:
                mappings['c'].remove(c)
            if c in mappings['f']:
                mappings['f'].remove(c)
        for c in list(digit):
            if c in mappings['a']:
                mappings['a'].remove(c)
            if c in mappings['b']:
                mappings['b'].remove(c)
            if c in mappings['d']:
                mappings['d'].remove(c)
            if c in mappings['e']:
                mappings['e'].remove(c)
            if c in mappings['g']:
                mappings['g'].remove(c)
def deduceFour(digit):
    if len(digit) == 4:
        decode[sortKey(digit)] = 4
        rdecode[4] = sortKey(digit)
        list_difference = [item for item in possibleVals if item not in list(digit)]
        for c in list_difference:
            if c in mappings['b']:
                mappings['b'].remove(c)
            if c in mappings['c']:
                mappings['c'].remove(c)
            if c in mappings['d']:
                mappings['d'].remove(c)
            if c in mappings['f']:
                mappings['f'].remove(c)
        for c in list(digit):
            if c in mappings['a']:
                mappings['a'].remove(c)
            if c in mappings['e']:
                mappings['e'].remove(c)
            if c in mappings['g']:
                mappings['g'].remove(c)
def deduceSeven(didgit):
    if len(digit) == 3: # is 7
        decode[sortKey(digit)] = 7
        rdecode[7] = sortKey(digit)
        list_difference = [item for item in possibleVals if item not in list(digit)]
        for c in list_difference:
            if c in mappings['a']:
                mappings['a'].remove(c)
            if c in mappings['c']:
                mappings['c'].remove(c)
            if c in mappings['f']:
                mappings['f'].remove(c)
        for c in list(digit):
            if c in mappings['b']:
                mappings['b'].remove(c)
            if c in mappings['d']:
                mappings['d'].remove(c)
            if c in mappings['e']:
                mappings['e'].remove(c)
            if c in mappings['g']:
                mappings['g'].remove(c)

total = 0
for line in input: 
    (signal, output) = line.split(" | ")

    decode = {}
    rdecode = {}

    possibleVals = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    mappings = {
        'a' : ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
        'b' : ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
        'c' : ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
        'd' : ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
        'e' : ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
        'f' : ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
        'g' : ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    }

    digits = list(map(lambda x : x.strip(), signal.split(" ")))
    for digit in digits:
        deduceOne(digit)
        deduceFour(digit)
        deduceSeven(digit)
        if len(digit) == 7:
            decode[sortKey(digit)] = 8
            rdecode[8] = sortKey(digit)
    
    three = None
    for digit in digits:
        if len(digit) == 5:
            # of 2, 3 and 5 only 3 intersects one
            if len(toSet(digit).intersection(toSet(rdecode[1]))) == 2:
                three = digit
                decode[three] = 3
                rdecode[3] = three
    
    b = toSet(rdecode[4]).difference(toSet(three))
    mappings['b'] = list(b)
    
    reduce(mappings)

    # 8 - (3 U 4) = e
    threeAndFour = toSet(rdecode[3]).union(toSet(rdecode[4]))
    e = toSet(rdecode[8]).difference(threeAndFour)
    mappings['e'] = list(e)

    reduce(mappings)

    six = None
    for digit in digits:
        if len(digit) == 6:
            # 6 U 3 == 8
            if len(toSet(digit).union(toSet(rdecode[1]))) == 7:
                six = digit
                decode[six] = 6
                rdecode[6] = six
    
    # 8 ^ 6 = c
    c = toSet(rdecode[8]).difference(toSet(six))
    mappings['c'] = list(c)

    reduce(mappings)

    res = 0
    for val in output.split(" "):
        
        res*=10
        res+=toNumber(val)

    total+=res
    print (res)
print(total)