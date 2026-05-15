n,s,t=map(int,input().split())
d=list(map(int,input().split()))

d.sort()
for i in range(n):
    if s>=d[i]:
        s+=d[i]
    else:
        break

if s>=t:
    print("Yes")
else:
    print("No")