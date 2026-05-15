n,m=map(int,input().split())

line=[list(map(int,input().split())) for i in range(m)]

ans=0
for i in range(1,n):
    for j in range(i+1,n+1):
        f=0
        for k in range(m):
            for l in range(n-1):
                if line[k][l]==i and line[k][l+1]==j:
                    f+=1
                    break
                if line[k][l]==j and line[k][l+1]==i:
                    f+=1
                    break
            if f==1:
                break
        if f==0:
            #print(i,j)
            ans+=1
print(ans)



