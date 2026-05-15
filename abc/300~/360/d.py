from bisect import bisect_right
n,t=map(int,input().split())
s=list(input())
ants=list(map(int,input().split()))
minus=[]
plus=[]
for i in range(n):
    if s[i]=="0":
        minus.append(ants[i])
    else:
        plus.append(ants[i])
for i in range(len(minus)):
    minus[i]-=2*t
minus.sort()
ans=0
for i in range(len(plus)):
    ans+=(bisect_right(minus,plus[i])-bisect_right(minus,plus[i]-2*t))
print(ans)


