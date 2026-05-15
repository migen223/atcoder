from sortedcontainers import SortedList
n,m,sx,sy=map(int,input().split())

xdic={}
ydic={}
for i in range(n):
    x,y=map(int,input().split())
    if x in xdic:
        xdic[x].add(y)
    else:
        xdic[x]=SortedList([y])
    if y in ydic:
        ydic[y].add(x)
    else:
        ydic[y]=SortedList([x])



def step(d,c):
    res=[0,0]
    if d=="U":
        res[1]+=c
    elif d=="D":
        res[1]-=c
    elif d=="R":
        res[0]+=c
    else:
        res[0]-=c
    return res

ans=set()
now=[sx,sy]
for i in range(m):
    #print(xdic)
    #print(ydic)
    x,y=now
    d,c=input().split()
    c=int(c)
    nx,ny=now[0]+step(d,c)[0],now[1]+step(d,c)[1]
    if d=="U" or d=="D":
        if x not in xdic:
            now=[nx,ny]
            continue
        
        lo=xdic[x].bisect_left(min(y,ny))
        up=xdic[x].bisect_right(max(y,ny))
        if lo>=len(xdic[x]):
            now=[nx,ny]
            continue
        dis=0
        for j in range(lo,up):
            if j>=len(xdic[x]):
                break
            dis+=1
        for j in range(dis):
            ans.add((x,xdic[x].pop(lo)))
        if len(xdic[x])==0:
            xdic.pop(x)

    elif d=="L" or d=="R":
        if y not in ydic:
            now=[nx,ny]
            continue
        lo=ydic[y].bisect_left(min(x,nx))
        up=ydic[y].bisect_right(max(x,nx))
        if lo>=len(ydic[y]):
            now=[nx,ny]
            continue
        dis=0
        for j in range(lo,up):
            if j>=len(ydic[y]):
                break
            dis+=1
        for j in range(dis):
            #print("ydicy",ydic[y][lo])
            ans.add((ydic[y].pop(lo),y))
        if len(ydic[y])==0:
            ydic.pop(y)
    now=[nx,ny]
    #print("now",now)
    #print("ans",ans)
    #print()
        
#print(ans)
now.append(len(ans))
print(*now)