
n,m,d=map(int,input().split())
t=list(map(int,input().split()))
ans=0
for i in range(n):
    if t[i]>m:
        if (t[i]-m)%d==0:
            ans+=(t[i]-m)//d
        else:
            ans+=(t[i]-m)//d+1
print(ans)