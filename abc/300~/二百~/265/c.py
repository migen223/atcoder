import sys
h,w=map(int,input().split())
grid=[list(input()) for i in range(h)]
now=[0,0]

visit=set(now)

for i in range(h*w+1):
    if grid[now[0]][now[1]]=="R":
        
        if now[1]==w-1:
            print(now[0]+1,now[1]+1)
            sys.exit()
        else:
            now[1]+=1
    elif grid[now[0]][now[1]]=="L":
        
        if now[1]==0:
            print(now[0]+1,now[1]+1)
            sys.exit()
        else:
            now[1]-=1
    elif grid[now[0]][now[1]]=="U":
        
        if now[0]==0:
            print(now[0]+1,now[1]+1)
            sys.exit()
        else:
            now[0]-=1
    elif grid[now[0]][now[1]]=="D":
        
        if now[0]==h-1:
            print(now[0]+1,now[1]+1)
            sys.exit()
        else:
            now[0]+=1
    if (now[0],now[1]) in visit:
        print(-1)
        sys.exit()
    else:
        visit.add((now[0],now[1]))
    #print(now)





