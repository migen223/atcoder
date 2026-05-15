
n,q=map(int,input().split())

pig={}
swap={}
rswap={}
for i in range(1,n+1):
    pig[i]=i
    swap[i]=i
    rswap[i]=i


for _ in range(q):
    que=list(map(int,input().split()))
    a=que[1]
    if que[0]==1:
        b=que[2]
        pig[a]=rswap[b]
    elif que[0]==2:
        b=que[2]
        s1=rswap[a]
        s2=rswap[b]
        rswap[a]=s2
        rswap[b]=s1
        swap[s1]=b
        swap[s2]=a
        
    else:
       
        #print(pig)
        print(swap[pig[a]])
        #print("ans",swap[pig[a]])
    #print("\n",swap,"\nrswap",rswap)

#print("\n",swap,"\nrswap",rswap)