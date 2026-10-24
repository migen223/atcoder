import sys
from itertools import product
parts=[]
for i in range(3):
    l=[]
    for j in range(4):
        l.append(list(input()))
    parts.append(l)

area=0
po=[[],[],[]]
for i in range(3):
    for j in range(4):
        for k in range(4):
            #print(parts[i])
            if parts[i][j][k]=="#":
                area+=1
                po[i].append([j,k])

def rotate(l):
    res=[]
    xmin=100
    ymin=100
    for y,x in l:
        res.append([x,-y])
        xmin=min(xmin,x)
        ymin=min(ymin,-y)
    #print(res)
    for i in range(len(l)):
        res[i][0]-=xmin
        res[i][1]-=ymin
    return res
    
def put(board,l,dy,dx):

    for y,x in l:
        ny,nx=y+dy,x+dx
        if 0<=ny<=3 and 0<=nx<=3:
            if board[ny][nx]=="#":
                return []
            board[ny][nx]="#"
            
        else:
            return []
    return board

if area==16:
    #for i in range(3):
        #print(*po[i])
        #print()
    pr=[[],[],[]]
    for i in range(3):
        l=po[i]
        pr[i].append(l)
        for j in range(3):
            l=rotate(l)
            pr[i].append(l)
            #print(*l)
        #print()
    #print(pr)
    
    for r1 in range(4):
        for r2 in range(4):
            for r3 in range(4):
                p1=pr[0][r1]
                p2=pr[1][r2]
                p3=pr[2][r3]
                for prod1 in product(range(4),repeat=2):
                    for prod2 in product(range(4),repeat=2):
                        for prod3 in product(range(4),repeat=2):
                            board=[[0 for _ in range(4)] for _ in range(4)]
                            board=put(board,p1,prod1[0],prod1[1])
                            if board:
                                board=put(board,p2,prod2[0],prod2[1])
                                if board:
                                    board=put(board,p3,prod3[0],prod3[1])
                                    if board:
                                        #print(board)
                                        print("Yes")
                                        sys.exit()
    print("No")

else:
    print("No")

                

    