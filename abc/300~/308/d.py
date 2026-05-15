import sys
h,w=map(int,input().split())
grid=[list(input()) for i in range(h)]


dy=[-1,1,0,0]
dx=[0,0,-1,1]

visit=[[0]*w for i in range(h)] 
visit[0][0]=1
def check(s1,s2):
    if (s1=="s" and s2=="n") or (s1=="n" and s2=="u") or(s1=="u" and s2=="k") or(s1=="k" and s2=="e") or (s1=="e" and s2=="s") :
        return True
    return False
        

if grid[0][0]=="s":
    visitable=[(0,0,"s")]
    while visitable:
        y,x,s=visitable.pop()
        for i in range(4):
            ny=y+dy[i]
            nx=x+dx[i]
            if 0<=ny<=h-1 and 0<=nx<=w-1:
                #print(s,grid[ny][nx],check(s,grid[ny][nx]),visit[ny][nx])
                if visit[ny][nx]==0 and check(s,grid[ny][nx]):
                    
                    visit[ny][nx]=1
                    visitable.append((ny,nx,grid[ny][nx]))
                    if ny==h-1 and nx==w-1:
                        print("Yes")
                        sys.exit()
        #print(visitable)
    print("No")
else:
    print("No")


