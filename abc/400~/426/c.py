
n,q=map(int,input().split())
pc=[1]*(n+1)
pc[0]=1
o=1
for i in range(q):
    x,y=map(int,input().split())
    res=0
    while o<=x:
        res+=pc[o]
        pc[y]+=pc[o]
        o+=1
    print(res)
"""
ika=[i+1 for i in range(n)]


left=0
l=[]
for i in range(q):
    x,y=map(int,input().split())
    x-=1
    #print(left)
    if left>x:
        print(0)
    else:
        left=x+1
        print(ika[x])
        for j in range(y-x-2):
            ika[left+j]-=ika[x]
    #print(ika)
"""




