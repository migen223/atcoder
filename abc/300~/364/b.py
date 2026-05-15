h,w=map(int,input().split())
taka=list(map(int,input().split()))
taka[0]-=1
taka[1]-=1
grid=[]
for i in range(h):
    c=list(input())
    grid.append(c)
#print(grid)
dx=[-1,0,1,0]#L,D,R,U
dy=[0,-1,0,1]
x=input()
for i in range(len(x)):
    if x[i]=="U" and taka[0]!=0:
        if grid[taka[0]-1][taka[1]]!="#":
            taka[0]-=1
            #print("U",taka)
    elif x[i]=="D" and taka[0]!=h-1:
        if grid[taka[0]+1][taka[1]]!="#":
            taka[0]+=1
            #print("D",taka)
    elif x[i]=="L" and taka[1]!=0:
        if grid[taka[0]][taka[1]-1]!="#":
            taka[1]-=1
           # print("L",taka)
    elif x[i]=="R" and taka[1]!=w-1:
        #print(*taka)
        if grid[taka[0]][taka[1]+1]!="#":
            taka[1]+=1
            #print("R",taka)
    #print(*taka)
taka[0]+=1
taka[1]+=1
print(*taka)

        