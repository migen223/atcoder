from math import ceil
n=int(input())
h=list(map(int,input().split()))
ans=0
if n==1:
    print(1)
else:
    for i in range(1,3000):
        jmax=0
        for j in range(min(i,n)):
            #print(j)
            a0=h[j]
            count=1
            #print(int(ceil(n/i)))
            for k in range(1,int(ceil(n/i))):
                #print(j+i*k)
                
                if j+i*k<n:
                    #print(a0,h[j+i*k],count)
                    if a0==h[j+i*k]:
                        count+=1
                        #print(count)
                    else:
                        jmax=max(jmax,count)
                        a0=h[j+i*k]
                        count=1
                jmax=max(jmax,count)
            #print(f"jない{jmax}")
        #print(f"iない{jmax}")
        ans=max(ans,jmax)
    print(ans)
"""
bils={}
for i in range(n):
    if h[i] in bils:
        bils[h[i]].append(i)
    else:
        bils[h[i]]=[i]
def tousa(l):
    ans=0
    for i in range(len(l)-2):
        #print(f"i={i}")
        for j in range(i+1,len(l)-1):
            #print(f"j={j}")
            count=2
            a0=l[i]
            a1=l[j]
            k=j+1
            d=a1-a0
            an=a1+d
            while k<len(l) and l[k]<=an:
                if an==l[k]:
                    count+=1
                    an+=d
                k+=1
                #print(count)
            ans=max(ans,count)
    return ans
ans=0
for i in bils:
    now=0
    #print(bils[i])
    if len(bils[i])==1:
        now=1
    elif len(bils[i])==2:
        now=2
    else:
        now=tousa(bils[i])
    ans=max(ans,now)
print(ans)
"""
