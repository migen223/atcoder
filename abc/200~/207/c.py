
n=int(input())

#t=1: [] 2:[) 3:(] 4:()

ans=0
seg=[]
for i in range(n):
    t,l,r=map(int,input().split())
    if l==r:
        if t==1:
            seg.append([l,r])
    else:
        if t==1:
            seg.append([l,r])
        elif t==2:
            seg.append([l,r-0.1])
        elif t==3:
            seg.append([l+0.1,r])
        elif t==4:
            seg.append([l+0.1,r-0.1])

for i in range(len(seg)-1):
    for j in range(i+1,len(seg)):
        if seg[i][0]<seg[j][0]:
            if seg[j][0]<=seg[i][1]:
                #print(seg[i],seg[j])
                ans+=1
        elif seg[j][0]<seg[i][0]:
            if seg[i][0]<=seg[j][1]:
                #print(seg[i],seg[j])
                ans+=1
        else:
            #print(seg[i],seg[j])
            ans+=1
print(ans)

