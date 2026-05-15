from bisect import bisect_left
n,q=map(int,input().split())
r=list(map(int,input().split()))
r.sort()
ruiseki=[0]
for i in r:
    ruiseki.append(ruiseki[-1]+i)
ruiseki.append(10**32)
for i in range(q):
    x=int(input())
    ans=bisect_left(ruiseki,x+1)-1
    print(ans)

