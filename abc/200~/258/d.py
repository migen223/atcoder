
n,x=map(int,input().split())

a=[]
b=[]
ab=[]
for i in range(n):
    an,bn=map(int,input().split())
    a.append(an)
    b.append(bn)
    ab.append(an+bn)

abr=[ab[0]]
for i in range(1,n):
    abr.append(abr[-1]+ab[i])


ans=10**36
ind=b.index(min(b))
for i in range(ind+1):
    ans=min(ans,abr[i]+(x-i-1)*b[i])
    #print(ans)

print(ans)
