from collections import deque
from bisect import bisect_left,bisect_right
from sortedcontainers import SortedList
import sys
s=list((input()))





a=SortedList([])
b=[]
c=SortedList([])
for i in range(len(s)):
    if s[i]=="A":
        a.add(i)
    elif s[i]=="B":
        b.append(i)
    else:
        c.add(i)

ans=0
for i in range(len(b)):
    nb=b[i]
    aind=a.bisect_left(nb)
    cind=c.bisect_left(nb)
    if aind==0 or len(c)==cind:
        continue
    #print(a,aind)
    #print(c,cind)
    a.discard(a[aind-1])
    c.discard(c[cind])
    ans+=1
    if len(a)==0 or len(c)==0:
        break
print(ans)


"""

if len(a)*len(b)*len(c)==0:
    print(0)
    sys.exit()
ans=0
for i in range(len(b)):
    nb=b[i]
    print(a[0],nb,c[-1])
    if a[0]>nb or c[-1]<nb:
        continue
    ans+=1

    a.popleft()
    c.pop()
    if len(a)==0 or len(c)==0:
        break

    print("a",a)
    print("c",c)

print(ans)



ans=0
while s[0]!="A":
    s.popleft()
    if len(s)==0:
        break
while s[-1]!="C":
    s.pop()
    if len(s)==0:
        break

while len(s)>=3:
    print(s)
    s.popleft()
    s.pop()
    while s[0]!="B" and s[-1]!="B":
        s.popleft()
        if len(s)==0:
            break
        s.pop()
        if len(s)==0:
            break
    if len(s)==0:
        break
    if s[0]=="B":
        s.popleft()
        ans+=1
    elif s[-1]=="B":
        s.popleft()
        ans+=1
    while s[0]!="A":
        s.popleft()
        if len(s)==0:
            break
    if len(s)==0:
        break
    while s[-1]!="C":
        s.pop()
        if len(s)==0:
            break
    if len(s)==0:
        break
    
print(ans)"""