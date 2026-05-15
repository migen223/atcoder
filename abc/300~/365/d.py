
n=int(input())
s=input()
dpp=[0]*n
dps=[0]*n
dpr=[0]*n

if s[0]=="R":
    dpp[0]=1
elif s[0]=="P":
    dps[0]=1
else:
    dpr[0]=1

for i in range(1,n):
    if s[i]=="R":
        dpr[i]=max(dpp[i-1],dps[i-1])
        dpp[i]=max(dpr[i-1],dps[i-1])+1
        dps[i]=-10**16
    elif s[i]=="P":
        dpp[i]=max(dps[i-1],dpr[i-1])
        dps[i]=max(dpr[i-1],dpp[i-1])+1
        dpr[i]=-10**18
    elif s[i]=="S":
        dps[i]=max(dpr[i-1],dpp[i-1])
        dpr[i]=max(dps[i-1],dpp[i-1])+1
        dpp[i]=-10**18
#print(dpr)
#print(dpp)
#print(dps)
print(max(dpr[-1],dps[-1],dpp[-1]))


