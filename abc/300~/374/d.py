from itertools import product,permutations
from math import sqrt
n,s,t=map(int,input().split())

line=[]
leng=[]
for i in range(n):
    a,b,c,d=map(int,input().split())
    line.append((a,b,c,d))
    leng.append(sqrt((a-c)**2+(b-d)**2)/t)
#print(line)
#print(leng)

ans=10**32
for p in permutations(range(n)):
    for bit in product([0,1],repeat=n):
        nans=0
        now=[0,0]
        for i in range(n):
            if bit[p[i]]==1:
                #print(sqrt((now[0]-line[p[i]][0])**2+(now[1]-line[p[i]][1])**2)/s)
                nans+=sqrt((now[0]-line[p[i]][0])**2+(now[1]-line[p[i]][1])**2)/s
                now[0]=line[p[i]][2]
                now[1]=line[p[i]][3]
            else:
                #print(sqrt((now[0]-line[p[i]][0])**2+(now[1]-line[p[i]][1])**2)/s)
                nans+=sqrt((now[0]-line[p[i]][2])**2+(now[1]-line[p[i]][3])**2)/s
                now[0]=line[p[i]][0]
                now[1]=line[p[i]][1]
            
            nans+=leng[p[i]]
            #print(now)
            #print(leng[p[i]])
        ans=min(ans,nans)
        #print(p,bit,nans)
print(ans)