import sys
sys.setrecursionlimit(10**7)
n=int(input())
a=list(map(int,input()))

def count(n):
    if n>=2:
        return 1
    else:
        return 0
    
def swap(l,to):
    res=[0,0]
    for i in l:
        res[i]+=1
    return max(0,2-res[to])


def open(l):
    if len(l)==1:
        return l[0]
    N=len(l)
    res=[0]*(N//3)
    for i in range(N):
        res[i//3]+=l[i]
    res=list(map(count,res))
    #print(res)
    return open(res)
o=(open(a)+1)%2
l=[]
for i in range((3**n)//3):
    nl=[]
    for j in range(3):
        nl.append(a[i*3+j])
    #print(nl,swap(nl,o))
    l.append(swap(nl,o))


def solve(l):
    if len(l)==1:
        return l[0]
    N=len(l)
    res=[]
    for i in range(N//3):
        nl=[]
        for j in range(3):
            nl.append(l[i*3+j])
        #print(nl,swap(nl,o))
        nl.sort()
        res.append(nl[0]+nl[1])
    return solve(res)

print(solve(l))

"""
vote=[[0,0] for i in range(3**(n-1))]
res=[0,0]
for i in range(3**n):
    if a[i]==0:
        vote[i//3][0]+=1
    else:
        vote[i//3][1]+=1
    if i%3==2:
        if  vote[i//3][0]>vote[i//3][1]:
            res[0]+=1
        else:
            res[1]+=1

lose=0
if res[0]>res[1]:
    lose+=1

change=[]
for i in range(3**(n-1)):
    if vote[i][lose]<=1:
        change.append(2-vote[i][lose])
change.sort(reverse=True)
ans=0
while res[lose]<=res[(lose+1)%2]:
    ans+=change.pop()
    res[lose]+=1
    res[(lose+1)%2]-=1
    #print(res,ans)
print(ans)

"""