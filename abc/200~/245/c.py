import sys
n,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
diffe=[]
an=[]
bn=[]
for i in range(n-1):
    an.append([abs(a[i]-a[i+1]),abs(a[i]-b[i+1])])
    bn.append([abs(b[i]-a[i+1]),abs(b[i]-b[i+1])])
an.extend(bn)
graph=[an,bn]


if n!=1:
    visit=set()
    next=0
    visitable=[]
    for i in range(2):
        if graph[0][0][i]<=k:
            visitable.append([0,0,i,0])
        if graph[1][0][i]<=k:
            visitable.append([1,0,i,0])

    while visitable:
        #print(visitable)
        now=visitable.pop()
        #print(now)
        visit.add(tuple(now))
        if graph[now[0]][now[1]][now[2]]<=k:
            if now[3]+1==n-1:
                print("Yes")
                sys.exit()
            else:
                for i in range(2):
                    #print((now[2],now[1]+1,i,now[3]+1))
                    if (now[2],now[1]+1,i,now[3]+1) not in visit:
                        visitable.append([now[2],now[1]+1,i,now[3]+1]) 
    print("No")   
else:
    print("Yes")        
                    
                        