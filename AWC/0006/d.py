from collections import deque
import sys
n,m=map(int,input().split())

sect=[]
for i in range(m):
    l,r=map(int,input().split())
    sect.append((l,r))
sect.sort()
sect=deque(sect)
now=1
ans=0
while now<=n:
    if len(sect)>0:
        ma=now
        while sect[0][0]<=now:
            l,r=sect.popleft()
            ma=max(ma,r+1)
            if len(sect)==0:
                break
        if ma==now:
            break
        now=ma
        ans+=1
    else:
        break
    #print(sect,now)


if now==n+1:
    print(ans)
else:
    print(-1)