
t=int(input())
for _ in range(t):
    n=int(input())
    s=input()

    a=[0]
    b=[0]
    c=[0]
    for i in range(n):
        if s[i]=="1":
            b.append(b[-1]+1)
            a.append(a[-1])
        else:
            a.append(a[-1]+1)
            b.append(b[-1])
        c.append(a[-1]-b[-1])
    ans=0
    ma=-10**32
    for i in range(n+1):
        if ma<c[i]:
            ans=min(ans,c[i]-ma)
            ma=c[i]
            
        else:
            ans=min(ans,c[i]-ma)
    print(b[-1]+ans)

"""
    if "1" in s:
        rle=[]
        now=[s[0],1]
        for i in range(1,n):
            if s[i]==now[0]:
                now[1]+=1
            else:
                rle.append((now[0],now[1]))
                now=[s[i],1]
        rle.append(now)
        if rle[0][0]=="0":
            rle.pop(0)
        if rle[-1][0]=="0":
            rle.pop()

        rabel={}
        ren0=[]
        for i in range(len(rle)):
            if i%2==0:
                rabel[i//2]=rle[i][1]
            else:
                ren0.append(rle[i][1])
        #print("ren0",ren0)
        ma=[10**32,-1]
        for i in rabel:
            if ma[1]<rabel[i]:
                ma=[i,rabel[i]]
        #print()
        #print(ma)
        #print(rabel)
        graph=[[] for i in range(len(rabel))]
        for i in range(len(rabel)-1):
            graph[i].append((i+1,ren0[i]))
            graph[i+1].append((i,ren0[i]))
        
        visit=[0]*len(rabel)
        visit[ma[0]]=1
        visitable=[(ma[0],0)]
        ans=0
        while visitable:
            now,score=visitable.pop()
            ans+=score
            for ne in graph[now]:
                if visit[ne[0]]==0:
                    visit[ne[0]]=1
                    visitable.append((ne[0],min(ne[1],rabel[ne[0]])))

        print(ans)
        #print("ans=",ans)
    else:
        print(0)
        #print("ans=",0)
    #print("\n graph",graph)
    
"""