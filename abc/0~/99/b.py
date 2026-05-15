a,b=map(int,input().split())
def sum1(n):
    ans=0
    for i in range(1,n+1):
        ans+=i
    return ans
origin=sum1(b-a)
print(origin-b)