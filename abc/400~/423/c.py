n,r=map(int,input().split())
l=list(map(int,input().split()))#0の時空いてる

close=[]
open=[]
for i in range(len(l)):
    if l[i]==1:
        close.append(i)
    else:
        open.append(i)
if len(open)==0:
    print(0)
elif len(open)==1:
    if open[0]<=r-1:
        print(2*((r-1)-open[0])+1)
    else:
        print(2*(open[0]-(r))+1)
else:
    first=open[0]
    end=open[-1]
    if r-2>=end:
        count=0
        for i in range(r-1,first-1,-1):
            if l[i]==1:
                count+=1
        print(r-1-first+1+count)
    elif first>=r:
        count=0
        for i in range(r,end+1):
            if l[i]==1:
                count+=1
        print(end-(r)+1+count)
    else:
        left=0
        right=0
        count=0
        for i in range(r-1,first-1,-1):
            if l[i]==1:
                count+=1
        left=r-1-first+1+count
        count=0
        for i in range(r,end+1):
            if l[i]==1:
                count+=1
        right=end-(r)+1+count
        #print(left,right)
        print(left+right)