n=int(input())
left=[]
right=[]
for i in range(n):
    l,r=map(int,input().split())
    left.append(l)
    right.append(r)
bottom=sum(left)
top=sum(right)
ans=[]
x=0
#print(bottom)
s=sum(left)
if bottom<=0 and top>=0:
    print("Yes")
    for i in range(n):
        d=min(right[i]-left[i],-s)
        s+=d
        #print(s)
        ans.append(left[i]+d)
    print(*ans)
    #print(sum(ans))
else:
    print("No")

"""
bottom=sum(left)
top=sum(right)
if bottom<=0 and top>=0:
    print("Yes")
    bottom=top=0
    rang=[]
    for i in range(n-1,0,-1): 
        #print(rang)
        bottom+=-right[i]
        top+=-left[i]
        rang.append([bottom,top])
        #print(bottom,top)
    rang.reverse()
    print(rang)
else:
    print("No")
"""