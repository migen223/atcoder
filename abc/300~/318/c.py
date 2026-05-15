n,d,p=map(int,input().split())
f=list(map(int,input().split()))

f.sort()
if n<=d:
    if sum(f)<=p:
        print(sum(f))
    else:
        print(p)
else:
    buy=0
    while len(f)>=d:
        s=0
        use=[]
        for i in range(d):
            q=f.pop()
            s+=q
            use.append(q)
        if s<p:
            for i in range(d):
                f.append(use[-1-i])
            break
        buy+=1
    if len(f)>=d:
        print(sum(f)+p*buy)
    else:
        print(min(sum(f),p)+p*buy)
    #print(f,buy)
    #print(sum(f)+p*buy)
    
            

        
