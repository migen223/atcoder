
n,x=map(int,input().split())
s=input()

k=0
while 2**k<=x:
    k+=1

k-=1
m=x%(2**k)
now=[k,m]

real=[s[0]]
for i in range(1,n):
    if len(real)>0:
        if (real[-1]=="R" or real[-1]=="L") and s[i]=="U":
            real.pop()
        else:
            real.append(s[i])
    else:
        real.append(s[i])

for i in range(len(real)):
    if real[i]=="U":
        now[0]-=1
        now[1]=now[1]//2
    elif real[i]=="L":
        now[0]+=1
        now[1]*=2
    else:
        now[0]+=1
        now[1]=now[1]*2+1
#print(real)
#print(now)
print(2**now[0]+now[1])


