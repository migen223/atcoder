from collections import Counter
n=int(input())
a=list(map(int,input().split()))

na=[]
for i in range(n):
    na.append(a[i]-(a[i]//200*200))

c=Counter(na)
ans=0
for mc in c.most_common():
    if mc[1]>=2:
        ans+=mc[1]*(mc[1]-1)//2
print(ans)