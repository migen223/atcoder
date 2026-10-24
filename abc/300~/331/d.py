
n,q=map(int,input().split())
grid=[input() for _ in range(n)]
r=[[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if grid[i][j]=="B":
            r[i][j]+=1
    

for i in range(n):
    for j in range(1,n):
        r[i][j]+=r[i][j-1]

for i in range(n):
    for j in range(1,n):
        r[j][i]+=r[j-1][i]

#print(r)

def calc(y,x):
    my,mx=y%n,x%n
    res=0
    res+=((x//n)*(y//n))*r[-1][-1]
    res+=(x//n)*r[my][-1]
    #print((x//n)*r[my][-1])
    res+=(y//n)*r[-1][mx]
    #print((y//n)*r[-1][mx])
    res+=r[my][mx]
    return res

for _ in range(q):
    a,b,c,d=map(int,input().split())
    ans=calc(c,d)
    if a!=0:
        ans-=calc(a-1,d)
    if b!=0:
        ans-=calc(c,b-1)
    if a!=0 and b!=0:
        ans+=calc(a-1,b-1)
    print(ans)
    
    