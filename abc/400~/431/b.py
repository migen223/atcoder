
x=int(input())
n=int(input())
w=list(map(int,input().split()))
q=int(input())

se=set()
ans=x

for i in range(q):
    p=int(input())-1
    if p not in se:
        ans+=w[p]
        se.add(p)
    else:
        ans-=w[p]
        se.remove(p)
    print(ans)

