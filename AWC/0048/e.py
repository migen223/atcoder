from itertools import product
n,k,m=map(int,input().split())
a=list(map(int,input().split()))
a=[a[i]%m for  i in range(n)]
mod=10**9+7

left=[]
right=[]
for i in range(n//2):
    right.append(a.pop())
left=[a[i] for i in range(len(a))]

ll=[{} for _ in range(k+1)]
rl=[{} for _ in range(k+1)]

if n%2==0:
    for p in product([0,1],repeat=n//2):
        lres=[0,0]
        rres=[0,0]
        for i in range(n//2):
            if p[i]==1:
                lres[0]+=1
                lres[1]+=left[i]
                lres[1]%=m
                rres[0]+=1
                rres[1]+=right[i]
                rres[1]%=m
        lk,lm=lres
        rk,rm=rres 
        if lk>k:
            continue
        if lm in ll[lk]:
            ll[lk][lm]+=1
        else:
            ll[lk][lm]=1
        if rm in rl[rk]:
            rl[rk][rm]+=1
        else:
            rl[rk][rm]=1
else:
    for p in product([0,1],repeat=n//2):
        
        rres=[0,0]
        for i in range(n//2):
            if p[i]==1:
                rres[0]+=1
                rres[1]+=right[i]
                rres[1]%=m
        rk,rm=rres 
        if rk>k :
            continue
        if rm in rl[rk]:
            rl[rk][rm]+=1
        else:
            rl[rk][rm]=1
        
    
    for p in product([0,1],repeat=n//2+1):
        lres=[0,0]
        for i in range(n//2+1):
            if p[i]==1:
                lres[0]+=1
                lres[1]+=left[i]
                lres[1]%=m
        lk,lm=lres 
        if lk>k :
            continue
        if lm in ll[lk]:
            ll[lk][lm]+=1
        else:
            ll[lk][lm]=1


#print(left)
#print(right)
#print(ll)
#print(rl)
ans=0
for i in range(k+1):
    for j in ll[i]:
        #print(i,j)
        #print(rl[k-i])
        for q in rl[k-i]:
            if (q+j)%m==0:
                ans+=ll[i][j]*rl[k-i][q]
                ans%=mod

print(ans)
                
