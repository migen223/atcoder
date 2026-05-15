
n=int(input())
h=list(map(int,input().split()))

now=0
ans=0
h.sort()
for i in range(n):
    ans+=abs(now-h[i])
    now=h[i]
print(ans+abs(now))