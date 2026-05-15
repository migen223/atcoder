n=int(input())
ans=0
for _ in range(n):
    a,b=map(int,input().split())
    if b<a:
        ans+=1
print