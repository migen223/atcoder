
n=int(input())
q=list(map(int,input().split()))
a=list(map(int,input().split()))
b=list(map(int,input().split()))

an=[]
for i in range(n):
    if a[i]!=0:
        an.append(q[i]//a[i])
    else:
        an.append(1000000000)
mi=min(an)
ans=-1
for i in range(mi+1):
    bn=[]
    for j in range(n):
        if b[j]!=0:
            bn.append((q[j]-a[j]*i)//b[j])
        else:
            bn.append(1000000000)
    bmi=min(bn)
    ans=max(ans,bmi+i)
print(ans)