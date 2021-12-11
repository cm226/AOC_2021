input = open("day10.dat", "r")

pairs = {
    '(':')',
    '{':'}',
    '[':']',
    '<':'>'
}

points = {
    ')':1,
    '}':3,
    ']':2,
    '>':4
}
scores = []
for line in input:
    stack = []
    line = line.strip()
    chars = list(line)
    for c in chars:
        if c in '({[<' : 
            stack.append(c)
            continue

        last = stack[-1:][0]
        if pairs[last] != c:
            stack = []
            break

        stack.pop()

    if(len(stack) != 0):
        stack.reverse()
        score = 0
        for c in stack:
            score*=5
            score+=points[pairs[c]]
        scores.append(score)

scores.sort()
print(scores[int(len(scores)/2)])
            