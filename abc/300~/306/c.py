n=int(input())
a=list(map(int,input().split()))

ans=[[] for i in range(n+1)]
for i in range(3*n):
    ans[a[i]].append(i+1)

mid=[]
for i in range(len(ans)-1):
    mid.append((ans[i+1][1],i+1))
mid.sort()
for i in range(n):
    print(mid[i][1],end=" ")

