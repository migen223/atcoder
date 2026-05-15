
n,k=map(int,input().split())
a=set(map(int,input().split()))
ans=10**32
socks=[]
for i in range(1,1+n):
    if i in a:
        socks.append(i)
    else:
        socks.append(i)
        socks.append(i)
if k%2==0:
    now=0
    for i in range(len(socks)//2):
        now+=socks[2*i+1]-socks[2*i]
    ans=min(ans,now)
else:
    sum01=[0]
    sum12=[0]
    for i in range(len(socks)//2):
        sum01.append(sum01[-1]+socks[2*i+1]-socks[2*i])
        sum12.append(sum12[-1]+socks[2*(i+1)]-socks[2*i+1])
    for i in range(len(socks)):
        now=0
        if i%2==0:
            now+=sum01[i//2]
            now+=sum12[-1]-sum12[i//2]
        else:
            now+=socks[i+1]-socks[i-1]
            now+=sum01[i//2]
            now+=sum12[-1]-sum12[i//2]
        ans=min(now,ans)
print(ans)

        