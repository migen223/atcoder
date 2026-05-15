from collections import Counter
n=int(input())
a=list(map(int,input().split()))

c=Counter(a)

def comb(n):
    if n<=0:
        return 0
    return (n*(n-1))//2
#print(c)
c[a[0]]-=1
if c[a[0]]==0:
    c.pop(a[0])
    ans=comb(n-1)
else:
    ans=comb(n-1-c[a[0]])+comb(c[a[0]])

minus=0
for mc in c.most_common():
    if mc[1]>=2:
        minus+=comb(mc[1])
ans-=minus

#print(ans)

for i in range(1,n):
    c[a[i]]-=1
    #print(minus)
    if c[a[i]]==0:
        c.pop(a[i])
        #print(comb(n-i-1)-minus,"ubsubse")
        ans+=comb(n-i-1)-minus
    else:
        
        ans+=comb(n-i-1-c[a[i]])-minus+comb(c[a[i]]+1)
        minus-=comb(c[a[i]]+1)-comb(c[a[i]])
        #print(comb(n-i-1-c[a[i]])-minus,"a12345678")
print(ans)


    
