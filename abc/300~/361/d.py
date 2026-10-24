import sys
from collections import deque,Counter
sys.setrecursionlimit(10**7)
n=int(input())
s=list(input())
t=list(input())
def tos(l):
    return "".join(l)
s.append(".")
s.append(".")
t.append(".")
t.append(".")
goal=tos(t)
if Counter(s)!=Counter(t):
    print(-1)
    sys.exit()
if n==2:
    if s==t:
        print(0)
    else:
        print(-1)
    sys.exit()
if s==t:
    print(0)
    sys.exit()

v=deque([[s,n,0]])
se=set([tos(s)])
while v:
    board,gap,dep=v.popleft()
    #print(tos(board),gap,dep)
    for i in range(n+1):
        if board[i]!="." and board[i+1]!=".":
            tg=gap
            nboard=[board[j]  for j in range(n+2)]
            nboard[gap],nboard[i]=nboard[i],nboard[gap]
            nboard[gap+1],nboard[i+1]=nboard[i+1],nboard[gap+1]
            gap=i
            sb=tos(nboard)
            #print(sb,se,sb not in se)
            if sb not in se:
                if sb==goal:
                    print(dep+1)
                    sys.exit()
                se.add(sb)
                v.append((nboard,gap,dep+1))
                
                #print("sb",sb)
            gap=tg


print(-1)