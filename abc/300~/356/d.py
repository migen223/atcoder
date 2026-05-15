
n,m=map(int,input().split())
count=m.bit_count()
p=998244353
m=format(m,'b')

def f(j,n):
    p2=2**j
    k=n//(2*p2)
    res=k*p2
    l=n%(2*p2)
    if (l>=p2):
        res+=(l-p2+1)
    return res

res=0
for i in range(len(m)):
    if m[-1-i]=="1":
        res+=f(i,n)
        res%=p
print(res)