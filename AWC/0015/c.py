from collections import Counter
n=int(input())

bt={}

for _ in range(n):
    p,q=map(int,input().split())
    if p in bt:
        bt[p].append(q)
    else:
        bt[p]=[q]

ans=0
for i in bt :
    num=len(bt[i])
    res=(num*(num-1))//2
    #print(bt[i])
    c=Counter(bt[i])
    #print(c)
    for co in c:
        res-=max(0,(c[co]*(c[co]-1))//2)
    ans+=res
    #print(res)

print(ans)
