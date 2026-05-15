
x=list(map(int,list(input())))
n=len(x)
ansl=[0]*(n+1)

for i in range(1,n+1):
    ansl[i]+=ansl[i-1]+x[i-1]

for i in range(n,0,-1):
    up=ansl[i]//10
    mod=ansl[i]%10
    ansl[i]=mod
    ansl[i-1]+=up

ans=[]
for i in range(n+1):
    if i==0 and ansl[i]==0:
        continue
    ans.append(str(ansl[i]))
print("".join(ans))

#349065850398865915384738153697722542688574377708317
#349065850398865915384738153697722542688574377708317
