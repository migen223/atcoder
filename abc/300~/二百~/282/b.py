
n,m=map(int,input().split())
people=[input() for i in range(n)]
ans=0
for i in range(n-1):
    for j in range(i+1,n):
        count=0
        for k in range(m):
            if people[i][k]=="o"  or people[j][k]=="o":
                count+=1
        if count==m:
            ans+=1
print(ans)