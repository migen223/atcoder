n,m=map(int,input().split())
s=input()
t=input()
sl=[0]*n
for _ in range(m):
    l,r=map(int,input().split())
    if l==r:
        sl[l-1]+=1
        if r!=n:
            sl[r]-=1
    elif r==n:
        sl[l-1]+=1
    else:
        sl[l-1]+=1
        sl[r]-=1

ans=[]
for i in range(1,n):
    sl[i]=sl[i]+sl[i-1]

for i in range(n):
    if sl[i]%2==0:
        ans.append(s[i])
    else:
        ans.append(t[i])

print("".join(ans))
