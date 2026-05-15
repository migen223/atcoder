
n,q=map(int,input().split())

l=[[-1,-1,i] for  i in range(n+1)] #(pre,aft,pos)

for i in range(q):
    c,p=map(int,input().split())
    #if l[c][0]!=-1:
     #   l[l[c][0]][1]=-1
    if l[c][1]!=-1:
        l[l[c][1]][0]=-1
    l[c][1]=p
    l[c][2]=l[p][2]
    l[p][0]=c
    
ans=[-1]*(n+1)
for i in range(1,n+1):
    if ans[i]<=0:
        team=[]
        team.append(i)
        v=[i]
        box=-1
        while v:
            now=v.pop()
            pre,aft,pos=l[now]
            if aft==-1:
                box=pos
                break
            if ans[aft]!=-1:
                box=ans[aft]
                break
            v.append(aft)
            team.append(aft)
        #print(team,box)
        for t in team:
            ans[t]=box

ansl=[0]*(n+1)
for i in range(1,len(ans)):
    ansl[ans[i]]+=1

#print(ans)
for i in range(1,n+1):
    print(ansl[i],end=" ")
print()
