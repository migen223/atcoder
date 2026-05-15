
n,k=map(int,input().split())

ans=[k]
for i in range(n):
    l=[]
    for j in ans:
        l.append(j//2)
        l.append(j-j//2)
    ans=l

if k%(2**n)==0:
    print(0)
else:
    print(1)
print(*ans)
