
n=int(input())
mod=998244353 
num=[0,0,0,0,0,0,0]
fact=[1,1,2]
for i in range(3,100):
    fact.append((fact[-1]*i)%mod)

for i in range(2,7):
    while n%i==0:
        num[i]+=1
        n//=i


cand=set()
def create(l):
    global cand
    #print("l",l)
    if l[2]*l[3]>=1:
        l[6]+=1
        l[2]-=1
        l[3]-=1
        tl=tuple(l)
        if tl not in cand:
            #print(l,tl)
            cand.add(tl)
            create(l)
        l[6]-=1
        l[2]+=1
        l[3]+=1
    if l[2]>=2:
        l[4]+=1
        l[2]-=2
        tl=tuple(l)
        if tl not in cand:
            cand.add(tl)
            create(l)
        l[4]-=1
        l[2]+=2

if n>1:
    print(0)
else:
    #print(num)
    ans=0
    cand.add(tuple(num))
    create(num)
    #print(cand)
    for c in cand:
        mole=0
        nume=1
        for i in c:
            mole+=i
            if i>=2:
                #print(fact[i],i)
                nume*=fact[i]
        nume*=5**mole
        mole=fact[mole]
        #print(nume)
        ans+=mole*pow(nume,-1,mod)
        ans%=mod
    print(ans)
        
        

    