
def sum3From(input, index):
    return int(input[index]) + int(input[index+1]) + int(input[index+2])

def getCount(input):
    count = 0
    prev = sum3From(input, 0)
    inputLen = len(input)
    for i,_ in enumerate(input[1:]):          
        if(inputLen - i < 3):
            break;
            
        cur = sum3From(input, i)

        if(cur > prev):
            count+=1
        prev = cur
    return count


text_file = open("day1.dat", "r")
lines = text_file.readlines()

print(getCount(lines))