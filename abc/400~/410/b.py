n,q=map(int,input().split())
x=list(map(int,input().split()))
box=[0]*n
ansl=[]
for i in range(q):
    if x[i]>=1:
        box[x[i]-1]+=1
        ansl.append(x[i])
    else:
        min1=min(box)
        #print(box)
        for w in range(n):
            if box[w]==min1:
                box[w]+=1
                ansl.append(w+1)
                break
    #print(box)
print(*ansl)
    