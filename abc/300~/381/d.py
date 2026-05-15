
n=int(input())
a=list(map(int,input().split()))

rle=[]

now=[a[0],1]
for i in range( 1,n):
    if now[0]!=a[i]:
        rle.append([now[0],now[1]])
        now=[a[i],1]
    else:
        now[1]+=1

rle.append([now[0],now[1]])

nrle=[]
for i in range(len(rle)):
    if rle[i][1]<=2:
        nrle.append(rle[i])
    else:
        nrle.append([rle[i][0],2])
        nrle.append([rle[i][0],2])

ans=0

#print(nrle)
l=0
r=0
se=set()
now=0
while r!= n-1 and l!=n-1:
    if nrle[r][1]==2:
        if nrle[r][0] not in se:
            se.add(nrle[r][0])
            now+=1
            ans=max(ans,now*2)
            r+=1
            if r==len(nrle):
                break
        else:
            se.remove(nrle[l][0])
            now-=1
            l+=1
            if l==len(nrle):
                break
    else:
        now=0
        se=set()
        r+=1
        l=r
        if r==(len(nrle)):
            break

    #print(r,l,se)
print(ans)






