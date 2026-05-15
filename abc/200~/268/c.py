#解説AC
n=int(input())
p=list(map(int,input().split()))

ans=0

count=[0]*n
for i in range(n):
    for j in range(3):
        count[(p[i]-i+j+n)%n]+=1
#print(count)
ans=0
for i in range(n):
    ans=max(ans,count[i])
print(ans)