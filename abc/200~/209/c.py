import sys
n=int(input())
c=list(map(int,input().split()))
p=10**9+7
se=set()

c.sort()
for i in range(n):
    if c[i]<i+1:
        print(0)
        sys.exit()
ans=1
for i in range(n):
    ans*=c[i]-(i)
    ans%=p
print(ans)
