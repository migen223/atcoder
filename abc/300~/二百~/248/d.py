from bisect import bisect_left,bisect_right
n=int(input())
a=list(map(int,input().split()))
q=int(input())
idx=[[] for i in range(n+1)]


for i in range(n):
    idx[a[i]].append(i)



for i in range(q):
    l,r,x=map(int,input().split())
    l-=1
    r-=1
    if len(idx[x])==0:
        print(0)
    else:
        left=bisect_left(idx[x],l)
        right=bisect_right(idx[x],r)
        print(right-left)


