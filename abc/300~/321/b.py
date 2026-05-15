n,x=map(int,input().split())
a=list(map(int,input().split()))

ans=99999999999999
for xn in range(101):
    a.append(xn)
    if sum(a)-max(a)-min(a)>=x:
        ans=min(ans,xn)
    a.pop()
if ans==99999999999999:
    print(-1)

else:
    print(ans)