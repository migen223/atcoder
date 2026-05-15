
n,d=map(int,input().split())

walls=[]
for i in range(n):
    l,r=map(int,input().split())
    walls.append((l,r))

walls.sort(key=lambda x:x[1])

ans=0
x=-10**32
for i in range(n):
    w=walls[i]
    if w[0]>x+d-1:
        x=w[1]
        ans+=1
    #print(x)

print(ans)








