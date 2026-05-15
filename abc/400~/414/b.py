n=int(input())
ans=""
al=0
f=0
for _ in range(n):
    l=list(input().split())
    al+=int(l[1])
    if al>100:
        f=1
        continue
    for i in range(int(l[1])):
        ans+=l[0]
if f==0:
    print(ans)
else:
    print("Too Long")