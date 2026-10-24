
n=int(input())
ans=[[] for _ in range(n)]
for i in range(n):
    l=list(map(int,input().split()))

    k=l[0]
    a=l[1:]
    for j in range(k):
        ans[a[j]-1].append(i+1)

for i in range(n):
    print(len(ans[i]),*ans[i])