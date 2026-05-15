import sys
n=int(input())
a=list(map(int,input().split()))
s=sum(a)
x=int(input())
ans=(x//s)*n
now=(x//s)*s
for i in range(n):
    if now>x:
        print(ans)
        sys.exit()
    else:
        now+=a[i]
        ans+=1
print(ans)