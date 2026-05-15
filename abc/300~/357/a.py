import sys
n,m=map(int,input().split())
h=list(map(int,input().split()))
ans=0
hands=0
for i in range(n):
    if hands+h[i]>m:
        print(ans)
        sys.exit()
    else:
        hands+=h[i]
        ans+=1
print(n)