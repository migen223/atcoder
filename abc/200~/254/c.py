import sys
from collections import Counter
n,k=map(int,input().split())

a=list(map(int,input().split()))
ac=[]
for i in a:
    ac.append(i)
ac.sort()

mod=[[] for i in range(k)]
mod2=[[] for i in range(k)]
for i in range(n):
    mod[i%k].append(a[i])
    mod2[i%k].append(ac[i])


for i in range(k):
    mod[i]=Counter(mod[i])
    mod2[i]=Counter(mod2[i])
    if mod[i]!=mod2[i]:
        print("No")
        sys.exit()
print("Yes")

