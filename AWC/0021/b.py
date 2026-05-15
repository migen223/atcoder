
n,m=map(int,input().split())
p=list(map(int,input().split()))

for _ in range(n):
    c=list(map(int,input().split()))
    if len(c)>=2:
        l=[]
        for i in range(1,len(c)):
            l.append((-p[c[i]-1],c[i]))
        l.sort()
        #print("l",l)
        print(l[0][1])
    else:
        print(0)
