
n,m=map(int,input().split())

ans=[]
for i in range(n):
    c,s=map(int,input().split())
    ans.append([c,s])

for i in range(n):
    c,s=ans[i]
    if c-s>=m:
        ans[i][1]+=m
        m=0
    else:
        ans[i][1]=ans[i][0]
        m-=c-s
    print(ans[i][1])

