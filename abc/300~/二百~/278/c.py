
n,q=map(int,input().split())

dic={}
se=set()
for i in range(q):
    t,a,b=map(int,input().split())
    
    if t==1:
        if a not in se:
            dic[a]=set()
            dic[a].add(b)
            se.add(a)
        else:
            dic[a].add(b)
    elif t==2:
        if a in se:
            if b in dic[a]:
                dic[a].remove(b)
    elif t==3:
        if a in se and b in se:
            if b in dic[a] and a in dic[b]:
                print("Yes")
            else:
                print("No")
        else:
            print("No")
    #print(dic)
    #print(se)
