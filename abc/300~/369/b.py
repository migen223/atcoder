n=int(input())
ans=0
left=-1
right=-1
for i in range(n):
    a,s=input().split()
    a=int(a)
    if s=="L":
        if left==-1:
            left=a
        else:
            ans+=abs(left-a)
            left=a
    else:
        if right==-1:
            right=a
        else:
            ans+=abs(right-a)
            right=a
print(ans)