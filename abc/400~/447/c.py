from collections import deque
s=list(input())
t=list(input())

sa=[]
ta=[]
for i in range(len(s)):
    if s[i]!="A":
        sa.append(s[i])
for i in range(len(t)):
    if t[i]!="A":
        ta.append(t[i])

s=deque(s)
t=deque(t)
#print(sa,ta)
if sa==ta:
    ans=0
    while t or s:
        if s[0]!=t[0]:
            if s[0]=="A":
                ans+=1
                s.popleft()
            elif t[0]=="A":
                ans+=1
                t.popleft()
        else:
            s.popleft()
            t.popleft()
        if len(s)==0 or len(t)==0:
            break
        #print(s,t)
    ans+=len(s)+len(t)
    print(ans)
else:
    print("-1")