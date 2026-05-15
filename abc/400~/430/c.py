from bisect import bisect_left
n,a,b=map(int,input().split())
s=list(input())

ans=0
l=0
r=0
ac=0
bc=0

br=[]
if s[0]=="b":
    br.append(1)
else:
    br.append(0)
for i in range(1,n):
    if s[i]=="b":
        br.append(br[-1]+1)
    else:
        br.append(br[-1])

ar=[]
if s[0]=="a":
    ar.append(1)
else:
    ar.append(0)
for i in range(1,n):
    if s[i]=="a":
        ar.append(ar[-1]+1)
    else:
        ar.append(ar[-1])

for i in range(n):
    if i==0:
        prea=preb=0
    else:
        prea=ar[i-1]
        preb=br[i-1]
    indb=bisect_left(br,preb+b)-1
    inda=bisect_left(ar,prea+a)
    #print(ind)
    ans+=max(0,indb-inda+1)
    #print(i,ans,inda,indb)

print(ans)

"""
while l!=n-1 or r!=n-1:
    if r<n-1:
        if s[r]=="a":
            r+=1
            ac+=1
            if bc<b and ac>=a:
                #print(l,r,bc,ac)
                ans+=1
        else:
            if bc+1>=b:
                if s[l]=="a":
                    ac-=1
                else:
                    bc-=1
                if bc<b and ac>=a:
                    ans+=1
                    #print(l+1,r,bc,ac)
                l+=1
            else:
                bc+=1
                r+=1
    else:
        if s[l]=="a":
            ac-=1
        else:
            bc-=1
        if bc<b and ac>=a:
            ans+=1
        l+=1
        
    print(l,r,ac,bc)
print(ans)
"""
            


