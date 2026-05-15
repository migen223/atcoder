from collections import Counter
n=int(input())
a=list(map(int,input().split()))

c=Counter(a)
ans=n*(n-1)//2

for mc in c.most_common():
    if mc[1]>=2:
        ans-=mc[1]*(mc[1]-1)//2
print(ans)

