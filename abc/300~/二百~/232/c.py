import sys
from collections import  Counter
from itertools import permutations
n,m=map(int,input().split())
ga=[set() for i in range(n+1)]
gb=[set() for i in range(n+1)]

for i in range(m):
    a,b=map(int,input().split())
    ga[a].add(b)
    ga[b].add(a)
for i in range(m):
    a,b=map(int,input().split())
    gb[a].add(b)
    gb[b].add(a)

for p in permutations(range(1,n+1)):
    f=0
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i!=j:
                if (j in ga[i])!=(p[j-1] in gb[p[i-1]]):
                    f+=1
    if f==0:
        print("Yes")
        sys.exit()
print("No")
                




"""
edgea=[len(ga[i]) for i in range(1,n+1)]
edgeb=[len(gb[i]) for i in range(1,n+1)]
#print(edgea,edgeb)
counta=[]
countb=[]
for i in range(1,n+1):
    la=[]
    for j in range(len(ga[i])):
        la.append(edgea[ga[i][j]-1])
        #print(la)
    la.sort()
    counta.append(tuple(la))
for i in range(1,n+1):
    lb=[]
    for j in range(len(gb[i])):
        lb.append(edgeb[gb[i][j]-1])
    lb.sort()
    countb.append(tuple(lb))
counta.sort()
countb.sort()
print(*counta)
print(*countb)

c1=Counter(edgea)
c2=Counter(edgeb)
if c1!=c2:
    print("No")
else:
    if counta==countb:
        print("Yes")
    else:
        print("No")

"""


