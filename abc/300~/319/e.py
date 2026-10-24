from math import lcm
n,x,y=map(int,input().split())

stop=[]
ps=set()
for i in range(n-1):
    p,t=map(int,input().split())
    stop.append((p,t))
    ps.add(p)
l=lcm(*list(ps))

def calc(n):
    ans=n+x
    for p,t in stop:
        if ans%p==0:
            ans+=t
        else:
            ans+=p-ans%p+t
    return ans+y

ansl=[]
for i in range(l):
    ansl.append(calc(i))
    #print(i,ansl[i])


Q=int(input())

for _ in range(Q):
    q=int(input())
    print(l*(q//l)+ansl[q%l])



"""
plus=[]
for i in range(1000):
    ans=[x+i]
    for p,t in stop:
        ans.append(ans[-1]+p-ans[-1]%p+t)
    print(i,*ans,ans[-1]-ans[0])
    plus.append(ans[-1]-ans[0])

rle=[]
l=[plus[0]]
for i in range(1,len(plus)):
    if plus[i]+1==l[-1]:
        l.append(plus[i])
    else:
        rle.append((l[0],l[-1],len(l)))
        l=[plus[i]]

for i in range(len(rle)):
    print(rle[i])
    


4 2 3
7 100
2 6
2 1
7
13
0
710511029
136397527
763027379
644706927
447672230


"""