
n=int(input())
a=list(map(int,input().split()))

ma=1+a[0]
ans=0
for i in range(n):
    if i+1<ma:
        ma=max(ma,i+1+a[i])
        ans+=1
    else:
        break
print(ans)