import sys
n,m=map(int,input().split())
if n==1:
    print(1)
    sys.exit()
w=list(map(int,input().split()))

ans=1
for i in range(n-1):
    if w[i]==1 :
        if m>=1:
            m-=1
        else:
            break
    ans+=1

print(ans)

