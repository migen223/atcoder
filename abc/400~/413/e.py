import sys
sys.setrecursionlimit(10**7)
t=int(input())

def merge(a,b):
    if a>b:
        for i in a:
            b.append(i)
        return b
    else:
        for i in b:
            a.append(i)
        return a

def solve(l):
    #print("l",l)
    if len(l)<2:
        return l
    res=[]
    for i in range(len(l)//2):
        res.append(merge(l[2*i],l[2*i+1]))
    #print("res",res)
    return solve(res)

for _ in range(t):
    n=int(input())
    p=list(map(int,input().split()))
    l=[]
    for i in range(2**n//2):
        res=[p[2*i],p[2*i+1]]
        res.sort()
        l.append(res)
    #print(l)
    #ans=solve(l)
    #print(ans)
    print(*solve(l)[0])
