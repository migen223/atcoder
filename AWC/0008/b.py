
n=int(input())
h=list(map(int,input().split()))
ans=0
bi=0
for i in range(n):
    if bi<h[i]:
        bi=h[i]
        ans+=1
print(ans)