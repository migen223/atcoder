import sys
from collections import Counter
h,w=map(int,input().split())
s1=[list(input()) for _ in range(h)]
s2=[list(input()) for _ in range(h)]

line1=[[] for i in range(w)]
line2=[[] for i in range(w)]
for i in range(h):
    for j in range(w):
        if s1[i][j]=="#":
            line1[j].append(i)
        if s2[i][j]=="#":
            line2[j].append(i)

l2s=set()
l2ls=[]
for i in range(w):
    l2s.add(tuple(line2[i]))
    l2ls.append(tuple(line2[i]))
l2c=Counter(l2ls)
#print(l2c)
#print(l2s)
for i in range(w):
    t=tuple(line1[i])
    if t in l2s:
        if l2c[t]==0:
            print("No")
            sys.exit()
        else:
            l2c[t]-=1
    else:
        print("No")
        sys.exit()
print("Yes")