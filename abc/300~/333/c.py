from itertools import product
"""
[1,1,1],[1,1,11],[1,11,11],[11,11,11],[1,1,111],[1,11,111],[11,11,111],[1,111,111],[111,111,111]
1 11 111 1111 4+4c2
           1
1+3+6+...+n+nC2(n+n(n-1)/2)
an=n+n(n-1)/2=(n^2+n)/2
sn=((n(n+1)(2n+1)/6+n(n+1)/2))/2
1,13,,23,33,113,123,133,223,233,333,1113,1123,1133
112222222233
"""
n=int(input())
ansl=[3]
l=["1","2","3"]
for i in range(2,13):
    for j in product(l,repeat=i):
        l1=list(j)
        #print(l1)
        #print(i)
        f=0
        for k in range(i-1):
            #print(k+1)
            if l1[k]>l1[k+1]:
                f+=1
                break
        if f==0 and l1[-1]=="3":
            ansl.append(int("".join(l1)))
print(ansl[n-1])

"""
def func(n):
    k=((n*(n+1)*(2*n+1)//6+n*(n+1)//2))//2
    return k
n=int(input())
k=0
while func(k) <n:
    k+=1
kotei=[]
for i in range(k):
    kotei.append("1")
big=int("".join(kotei))
kouho=[]
for i in range(1,k+1):
    ap=""
    for j in range(i):
        ap+="1"
    kouho.append(ap)
now=1

    print(list(i))
    if now==n-func(k-1):
        l=list(i)
        print(int(l[0])+int(l[1])+big)
        print(now,l[0],l[1],n-func(k-1))
        break
    else:
        now+=1
"""