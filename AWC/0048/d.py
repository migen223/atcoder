
n,m,K=map(int,input().split())

def toint(s):
    res=[]
    for i in s:
        res.append(int(i))
    return res

s=[input() for i in range(n)]
grid=[toint(s[i]) for i in range(n)]
r=[[0 for _ in range(m+1)] for _ in range(n+1)]
for i in range(n):
    for j in range(m):
        r[i+1][j+1]=grid[i][j]

for i in range(n+1):
    for j in range(1,m+1):
        r[i][j]+=r[i][j-1]
for i in range(m+1):
    for j in range(1,n+1):
        r[j][i]+=r[j-1][i]
#print(r)
ans=-1
for i in range(1,1+n):
    for j in range(1,1+m):
        if (i*j)==K:
            #print("i,j",i,j)
            for k in range(n-i+1):
                for l in range(m-j+1):
                    #print(i+k,j+l,k,l,"aij",r[i+k][j+l],r[k][j+l],r[i+k][l],r[k][l])
                    res=0
                    res+=r[i+k][j+l]-r[k][j+l]-r[i+k][l]+r[k][l]
                    ans=max(ans,res)

print(ans)
                

            