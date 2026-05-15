"""
n=int(input())
flavor=[set() for i in range(n+1)]
fd=[]
deli=[]
fkind=set()
for i in range(n):
    f,s=map(int,input().split())
    fd.append([f,s])
    flavor[f].add(s)
    deli.append(s)
    fkind.add(f)

if len(fd)>2:
    if len(fkind)>=2:
        ma=max(deli)
        maxlist=[] #(flavor)
        for i in range(n):
            if fd[i][1]==ma:
                maxlist.append(fd[i][0])
        deli.sort()
        ans=deli.pop()
        now=deli[-1]
        plus=0
        for i in range(len(maxlist)):
            iplus=0
            count=0
            if now in flavor[maxlist[i]]:
                f=0
                for j in range(1,len(deli)):
                    if deli[-1-j] not in flavor[maxlist[i]] or count+1>len(flavor[maxlist[i]]):
                        iplus=max(deli[-j-1],now//2)
                        f+=1
                        break
                    else:
                        count+=1
                if f==0:
                    iplus=now//2
            else:
                iplus=now
            plus=max(plus,iplus)
        print(ans+plus)
    else:
        deli.sort()
        print(deli.pop()+deli.pop()//2)
else:
    if fd[0][0]==fd[1][0]:
        print(max(deli)+min(deli)//2)
    else:
        print(sum(deli))
"""
n=int(input())
ans=0
flavor=[[] for _ in range(n+1)]


for i in range(n):
    f,s=map(int,input().split())
    flavor[f].append(s)

for i in range(n+1):
    flavor[i].sort()
    if len(flavor[i])>1:
        ans=max(ans,flavor[i][-1]+flavor[i][-2]//2)

maxl=[]
for i in range(n+1):
    if len(flavor[i])!=0:
        maxl.append(max(flavor[i]))
maxl.sort()
if len(maxl)>=2:
    ans=max(ans,maxl[-1]+maxl[-2])

print(ans)