from itertools import product
n,x=map(int,input().split())

balln=[]
balls=[]

for i in range(n):
    que=list(map(int,input().split()))
    l=que.pop(0)
    balln.append(l)
    que.sort()
    balls.append(que)

l=[range(balln[i]) for i in range(n)]

ans=0
for p in product(*l):
    pro=balls[0][p[0]]
   # print(p)
    for j in range(1,n):
        pro*=balls[j][p[j]]
    if pro==x:
        ans+=1
print(ans)


