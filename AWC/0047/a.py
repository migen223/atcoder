
n,k=map(int,input().split())

ts=[]
for i in range(n):
    t=int(input())
    ts.append(t)
ans=0
for i in range(1,n):
    if abs(ts[i]-ts[i-1])>=k:
        ans+=1

print(ans)