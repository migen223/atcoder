from collections import Counter
n=int(input())
s=input()
c=Counter(s)
ma=int("".join(sorted(list(s),reverse=True)))
#print(ma)
ans=0
for i in range(10**(n//2+1)+1):
    if i**2>ma:
        break
    
    ns=str(i**2)
    cn={}
    for j in ns:
        if j in cn:
            cn[j]+=1
        else:
            cn[j]=1
    
    if len(ns)!=n:

        if "0" not in cn:
            cn["0"]=n-len(ns)
        else:
            cn["0"]+=n-len(ns)

    if cn==c:
        ans+=1
    #print(i**2)
    #print(cn)


print(ans)
