
n,k=map(int,input().split())

mall=[]
for _ in range(n):
    q=list(map(int,input().split()))
    p=q[2:]
    mall.append(sum(p)-q[0])

mall.sort(reverse=True)
#print(mall)
ans=0
for i in range(k):
    if mall[i]<0:
        break
    ans+=mall[i]

print(max(0,ans))

