

n,m=list(map(int,input().split()))

color=input().split()
pcolor=input().split()
price=list(map(int,input().split()))

dic={}
se=set()
for i in range(1,m+1):
    dic[pcolor[i-1]]=price[i]

ans=0

for i in range(n):
    if color[i] in pcolor:
        ans+=dic[color[i]]
    else:
        ans+=price[0]
print(ans)


