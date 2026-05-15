
t=int(input())
for _ in range(t): 
    n=int(input())
    a=list(map(int,input().split()))
    ban=set()
    for i in range(2*n-1):
        if a[i]==a[i+1]:
            ban.add(a[i])
    a.append(-1)
    dic={}
    dic[a[0]]=[(-2,a[1])]
    for i in range(1,2*n):
        if a[i] not in dic:
            dic[a[i]]=[(a[i-1],a[i+1])]
        else:
            dic[a[i]].append((a[i-1],a[i+1]))
    #print("\n",dic)
    ans=0
    se=set()
    for i in dic:
        if i not in ban:
            now=dic[i]
            for j in now[0]:
                if j>0:
                    if j in now[1] and j not in ban:
                        if i in dic[j][0] and i in dic[j][1] and (i,j) not in se:
                            ans+=1
                            se.add((i,j))
                            #print(i,j)
    #print(ban)
    print(ans//2)
   # print("ans",ans)
