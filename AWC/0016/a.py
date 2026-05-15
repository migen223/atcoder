
n=int(input())
ans=[0,0]
for i in range(n):
    a,b=map(int,input().split())
    if a>b:
        ans[0]+=1
        ans[1]+=a-b

print(*ans)