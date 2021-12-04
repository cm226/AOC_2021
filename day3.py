import math

def mostCommon(input, index):
    count = 0
    for entry in input:
        count += int(entry[index])
    
    if(count >= int(math.ceil(len(input)/2))):
        return 1

    return 0

def strToBin(str):
    res = 0
    for c in str:
        res = res << 1
        res += int(c)
    return res

text_file = open("day3.dat", "r")
lines = text_file.readlines()

oxGen = lines
scrub = lines

numBits = 12
for i in range(numBits):
    common = mostCommon(oxGen, i)       
    oxGen = list(filter(lambda x: (x[i] == str(common)), oxGen))
    if(len(oxGen) == 1):
        break
    
for i in range(numBits):
    common = mostCommon(scrub, i)
    leastCommon = (common+1)%2
    scrub = list(filter(lambda x: (x[i] == str(leastCommon)), scrub))
    if(len(scrub) == 1):
        break


ox = strToBin(oxGen[0].strip())
sc = strToBin(scrub[0].strip())

print (ox * sc)