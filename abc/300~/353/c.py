from bisect import bisect_left
n=int(input())
a=list(map(int,input().split()))
mod=10**8
a.sort()

ans=sum(a)*(n-1)
count=0
for i in range(n-1):
    ind=bisect_left(a,mod-a[i],lo=i)
    if ind==i:
        count+=(n-i-1)
    else:
        count+=n-ind
#print(count)
print(ans-(mod)*count)
        

    




"""
5
1 3 99999999 99999994 1000000

"""