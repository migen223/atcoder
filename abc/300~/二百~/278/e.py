
h,w,n,h0,w0=map(int,input().split())

grid=[list(map(int,input().split())) for i in range(h)]
dic={}
for i in range(h):
    for j in range(w):
        if grid[i][j] not in dic:
            dic[grid[i][j]]=1
        else:
            dic[grid[i][j]]+=1

r=[[[0]*(n+1) for _ in range(w)] for i in range(h)]
for i in range(h):
    r[i][0][grid[i][0]]=1
for i in range(h):
    for j in range(w-1):
        for k in range(1,1+n):
            r[i][j+1][k]=r[i][j][k]
        r[i][j+1][grid[i][j+1]]+=1

for i in range(h-1):
    for j in range(w):
        for k in range(1,n+1):
            r[i+1][j][k]+=r[i][j][k]

"""
for i in range(h):
    for j in range(w):
        l=[]
        for k in range(1,n+1):
            l.append(str(r[i][j][k]))
        print("".join(l),end=" ")
    print()

#print(dic)
l=[0]*(n+1)
for i in dic:
    l[i]=dic[i]
print(r[-1][-1])
print(l)
"""

ansl=[[0]*(w-w0+1) for i in range(h-h0+1)]
for i in range(h-h0+1):
    for j in range(w-w0+1):
        #ban=r[i+h0-1][j+w0-1]
        ban=[r[i+h0-1][j+w0-1][k] for k in range(n+1)]
        #print(i,j,ban)
        if i!=0:
            for k in range(1,n+1):
                ban[k]-=r[i-1][j+w0-1][k]
            #print(i,j,ban,r[i-1][j+w0-1],i-1,j+w0-1)
        if j!=0:
            for k in range(1,n+1):
                ban[k]-=r[i+h0-1][j-1][k]
            #print(i,j,ban,r[i+h0-1][j-1],i+h0-1,j-1)
        if i*j!=0:
            for k in range(1,n+1):
                ban[k]+=r[i-1][j-1][k]
            #print(i,j,ban)
        #print(i,j,ban)
        ans=len(dic)
        for k in dic:
            if dic[k]==ban[k]:
                ans-=1
        ansl[i][j]=ans

for i in range(h-h0+1):
    print(*ansl[i])
