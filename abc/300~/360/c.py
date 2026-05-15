n=int(input())
box=[[] for _ in range(n+1)]
a=list(map(int,input().split()))
w=list(map(int,input().split()))
ans=0

#print(box)
for i in range(n):
    #print(a[i],w[i])
    #print(box[a[i]])
    box[a[i]].append(w[i])
    #print(box[a[i]])
    #print(box)
#print(box)


for i in range(n+1):
    
    if len(box[i])>=2:
        box[i].sort()
        s=sum(box[i])
        ans+=s-box[i][-1]
        #print(ans)
print(ans)