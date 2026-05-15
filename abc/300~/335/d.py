n=int(input()) 
ans=[[0 for i in range(n)] for i in range(n)]
now=[0,0]
visit=set()
visit.add((0,0))
ans[0][0]=1
f=0
dy=[0,1,0,-1]
dx=[1,0,-1,0]


for i in range(2,n*n):
    if f==0:
        if now[1]+1<=n-1 and (now[0],now[1]+1) not in visit:
            now[1]+=1
            ans[now[0]][now[1]]=i
            visit.add((now[0],now[1]))
        else:
            f=(f+1)%4
            now[0]+=1
            ans[now[0]][now[1]]=i
            visit.add((now[0],now[1]))
    elif f==1:
        if now[0]+1<=n-1 and (now[0]+1,now[1]) not in visit:
            now[0]+=1
            ans[now[0]][now[1]]=i
            visit.add((now[0],now[1]))
        else:
            f=(f+1)%4
            now[1]-=1
            ans[now[0]][now[1]]=i
            visit.add((now[0],now[1]))
    elif f==2:
        if now[1]-1>=0 and (now[0],now[1]-1) not in visit:
            now[1]-=1
            ans[now[0]][now[1]]=i
            visit.add((now[0],now[1]))
        else:
            f=(f+1)%4
            now[0]-=1
            ans[now[0]][now[1]]=i
            visit.add((now[0],now[1]))
    elif f==3:
        if now[0]-1>=0 and (now[0]-1,now[1]) not in visit:
            now[0]-=1
            ans[now[0]][now[1]]=i
            visit.add((now[0],now[1]))
        else:
            f=(f+1)%4
            now[1]+=1
            ans[now[0]][now[1]]=i
            visit.add((now[0],now[1]))

ans[n//2][n//2]="T"
for i in range(n):
    print(*ans[i])






"""
1 2 3 
8 T 4
7 6 5
"""
