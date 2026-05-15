from bisect import bisect_left
n,q=map(int,input().split())
s=list(input())
ren=[]
for i in range(n-1):
    if s[i]==s[i+1]:
        ren.append(i)
for i in range(q):
    l,r=map(int,input().split())
    print(bisect_left(ren,r-1)-bisect_left(ren,l-1))