import sys
n,w=map(int,input().split())
cheese=[]
for i in range(n):
    c=list(map(int,input().split()))
    cheese.append(c)

cheese.sort()
#print(cheese)
now=0
ans=0
while cheese:
    if w-now>=cheese[-1][1]:
        now+=cheese[-1][1]
        ans+=cheese[-1][1]*cheese[-1][0]
        cheese.pop()
    else:
        ans+=cheese[-1][0]*(w-now)
        print(ans)
        sys.exit()


print(ans)


