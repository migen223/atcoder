import copy,sys
n=int(input())
a=list(map(int,input().split()))
a.insert(0,0)
ans=[]


for i in range(1,n+1):
    visitable=[[i,{},0,[]]]
    visit=set()
    while visitable:
        now=visitable.pop()
        visit.add(now[0])
        now[1][now[0]]=now[2]
        now[3].append(now[0])
        now[2]+=1
        #print(now)
        if a[now[0]] in visit:
            #print(now)
            print(len(now[3])-now[1][a[now[0]]])
            print(*now[3][now[1][a[now[0]]]:])
            sys.exit()
        else:
            visitable.append([a[now[0]],now[1],now[2],now[3]])


"""
for i in range(n):
    visitable=[[i,i,[]]]
    visit=set()
    while visitable:
        now=visitable.pop()
        visit.add(now[0])
        now[2].append(now[0])
        if a[now[0]-1]==now[1]:
            print(len(now[2]))
            print(*now[2])
            sys.exit()
        elif a[now[0]-1] not in visit:
            visitable.append([a[now[0]-1],i,now[2]])
        """
