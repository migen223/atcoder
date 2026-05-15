n=int(input())
a=list(map(int,input().split()))
ma=max(a)
an=0
ans=0
for i in range(n):
    if a[i]==ma:
        continue
    else:
        an=max(an,a[i])

print(an)
