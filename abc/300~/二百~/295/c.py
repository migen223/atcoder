from collections import Counter
n=int(input())
ans=0
s=list(map(int,input().split()))
cs=Counter(s)
ans=0
for i in cs:
    if cs[i]>=2:
        ans+=cs[i]//2
print(ans)

