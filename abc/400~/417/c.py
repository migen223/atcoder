from collections import Counter
n = int(input())
a = list(map(int, input().split()))

l=[]
l2=[]
for i in range(n):
    l.append((i+1)-a[i])
    l2.append(a[i]+i+1)
c=Counter(l)
c2=Counter(l2)
#print(l)
#print(c)
#print(c2)
ans=0

for mc in c.most_common():
    if mc[0]==1:
        ans+=mc[0]*(mc[0]-1)//2
    else:
        if mc[0] in c2:
            ans+=mc[1]*c2[mc[0]]
print(ans)
