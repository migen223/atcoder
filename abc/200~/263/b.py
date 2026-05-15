
n=int(input())
p=list(map(int,input().split()))

ans=0
people=[-1]*(n+1)

for i in range(2,n+1):
    people[i]=p[i-2]
now=n
while now!=1:
    now=people[now]
    ans+=1
print(ans)
