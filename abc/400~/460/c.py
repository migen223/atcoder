from bisect import bisect_right
n,m=map(int,input().split())
a=list(map(int,input().split()))#シャリ
b=list(map(int,input().split()))#ネタ

a.sort()
b.sort()

ans=0
s=0
for i in range(n):
    ind=bisect_right(b,a[i]*2)
    if s<ind:
        s+=1
        ans+=1


print(ans)
