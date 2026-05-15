

n=int(input())
x=list(map(int,input().split()))
x.sort()
for i in range(n):
    x.pop()
ans=0
for i in range(n,4*n):
    ans+=x[i]
    #print(x[i])
#print(ans)
print(ans/(3*n))