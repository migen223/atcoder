n=int(input())
ans=1
for _ in range(n):
    i =input()
    l=list(map(int,i.split()))
    su=sum(l)
    ans*=su
print(ans%(10**9+7))
