

tl = [20,-5]
br = [30,-10]

sx = br[0] - tl[0]
sy = tl[1] - br[1]

def isIn(x,y):
    tx = x - tl[0]
    ty = y - br[1]

    return tx >= 0 and tx <= sx and ty >= 0 and ty <= sy

if tl[1] >=0 and br[1] <=0:
    print("max height infinate")
    exit

if tl[1] < 0:
    # max y set bound by delta of start and bottom y
    maxY = -br[1]

if br[1] > 0:
    maxY = tl[1]


cx = br[0]
cy = maxY

done = False
count = 0
while not done:
    pos = [0,0]
    vel = [cx, cy]
    
    while pos[1] > br[1] or vel[1] > 0:
        pos[0] += vel[0]
        pos[1] += vel[1]

        vel[1] -= 1
        if vel[0] != 0:
            if vel[0] < 0:
                vel[0]+=1
            else:
                vel[0]-=1
        
        if isIn(pos[0], pos[1]):
            count+=1
            break

    cx-=1
    if cx == 0:
        cy-=1
        cx = br[0]

    if cy < br[1]:
        done = True
    
print (count)
