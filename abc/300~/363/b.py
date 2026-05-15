n,t,p=map(int,input().split())
l=list(map(int,input().split()))
count=0
day=0
for i in range(n):
    if l[i]>=t:
        count+=1
if count>=p:
    print(0)
else:
    for i in range(t):
        count=0
        for j in range(n):
            l[j]+=1
            if l[j]>=t:
                count+=1
        day+=1
        if count>=p:
            break
        
        #print(l,count)
    print(day)
