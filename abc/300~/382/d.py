
n,m=map(int,input().split())

ran=[]
for i in range(1,n+1):
    ran.append((1+10*(i-1),m-10*(n-i)))
ansl=[]

visitable=[([i],1) for i in range(ran[0][0],ran[0][1]+1)]

while visitable:
    now=visitable.pop()
    l=now[0]
    depth=now[1]
    
    if depth!=n:
        for j in range(l[-1]+10,ran[depth][1]+1):
            nl=[l[i] for i in range(len(l))]
            nl.append(j)
            visitable.append((nl,depth+1))
    else:
        ansl.append(tuple([l[i] for i in range(len(l))]))
    #print(visitable)

ansl.sort()
print(len(ansl))
for i in range(len(ansl)):
    print(*ansl[i])


