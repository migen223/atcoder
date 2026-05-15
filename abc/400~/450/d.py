
n,k=map(int,input().split())
a=list(map(int,input().split()))
ma=[a[i]%k for i in range(n)]
se=set(ma)
ma=list(se)
ma.sort()
n=len(ma)

for i in range(n):
    ma.append(ma[i]+k)
#print(ma,n)
ans=10**32

for i in range(n+1):
    #print(n+i-1,i,ma[n+i-1],ma[i])
    ans=min(ma[n+i-1]-ma[i],ans)
print(ans)

"""
3 1 9
1 3 9  11 13 19

0 4 5 6 10 11

"""