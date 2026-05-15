
n,W=map(int,input().split())

tape=[]
wall=[]
for i in range(n):
    l,w=map(int,input().split())
    tape.append((l,l+w))

tape.sort()

for i in range(n):
    l,r=tape[i]

    if len(wall)==0:
        wall.append(l)
        wall.append(r)
    else:
        if wall[-1]<l:
            wall.append(l)
            wall.append(r)
        else:
            wall[-1]=max(wall[-1],r)
        
ans=0
for i in range(len(wall)//2):
    ans+=wall[2*i+1]-wall[2*i]
print(ans)
