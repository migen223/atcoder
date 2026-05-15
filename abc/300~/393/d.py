n=int(input())
s=list(input())
ans=0
ind1=[]
for i in range(n):
    if s[i]=="1":
        ind1.append(i)
inuber=len(ind1)
#print(ind1)
if inuber==1:
    print(0)
elif inuber==2:
    print(ind1[1]-ind1[0]-1)
else:
    mid=len(ind1)//2
    #print(mid)
    for i in range(len(ind1)):
        
        if i!=mid:
            if i<mid:
                #print(ind1[mid]-ind1[i]-(mid-i))
                ans+=ind1[mid]-ind1[i]-(mid-i)
            else:
                #print(ind1[i]-ind1[mid]-(i-mid))
                ans+=ind1[i]-ind1[mid]-(i-mid)
    print(ans)
