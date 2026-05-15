from itertools import permutations
n=int(input())
runer=[]
for _ in range(n):
    i=input()
    l=list(map(int,i.split()))
    runer.append(l)
m=int(input())
badmember=[]
for _ in range(n):
    b=set()
    badmember.append(b)

for _ in range(m):
    x,y=map(int,input().split())
    badmember[x-1].add(y-1)
    badmember[y-1].add(x-1)
    
q=[]
min=10**10
for i in range(n):
    q.append(i)
for p in permutations(q,n):
    member=list(p)
    f=0
    time=0
    for i in range(len(member)-1):
        if member[i+1] in badmember[member[i]]:
            f+=1
            break
    if f!=0:
        continue
    for j in range(len(member)):
        time+=runer[member[j]][j]
    if time<min:
        min=time
if min==10**10:
    print(-1)
else:
    print(min)
    

    

