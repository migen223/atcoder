from collections import Counter
n=int(input())
a=list(map(int,input().split()))
p= 998244353

r=[a[0]]
for i in range(1,n):
    r.append(r[-1]+a[i])

l1=[10**i for i in range(1,11)]
l2=[]
for i in range(n-1):
    l=[]
    for j in l1:
        l.append(a[i]*j)
    l2.append(l)

keta=[len(str(a[i])) for i in range(1,n)]
c=Counter(keta)
ketas=[]
for i in range(1,n):
    dic={}
    for j in c:
        dic[j]=c[j]
    ketas.append(dic)
    if c[keta[i-1]]==1:
        c.pop(keta[i-1])
    else:
        c[keta[i-1]]-=1

#print(l2)

#print(l2)
ans=0
for i in range(n-1):
    ans+=r[-1]-r[i]
    for j in ketas[i]:
        #print(i,j)
        ans+=ketas[i][j]*l2[i][j-1]
        ans%=p
print(ans%p)
