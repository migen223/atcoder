
n,a,b=map(int,input().split())

grida=[[0]*(n+2) for i in range(n+2)]
gridt=[[0]*(n+2) for i in range(n+2)]
for i in range(a):
    r1,c1,r2,c2=map(int,input().split())
    gridt[r1][c1]+=1
    gridt[r2+1][c1]-=1
    gridt[r1][c2+1]-=1
    gridt[r2+1][c2+1]+=1

for i in range(b):
    r1,c1,r2,c2=map(int,input().split())
    grida[r1][c1]+=1
    grida[r2+1][c1]-=1
    grida[r1][c2+1]-=1
    grida[r2+1][c2+1]+=1
"""
for i in range(n+1):
    for j in range(n+1):
        print(grida[i][j],end="")
    print()
print()
for i in range(n+1):
    for j in range(n+1):
        print(gridt[i][j],end="")
    print()
print()"""

for i in range(1,n+1):
    for j in range(2,n+1):
        grida[i][j]+=grida[i][j-1]
        gridt[i][j]+=gridt[i][j-1]

for i in range(1,n+1):
    for j in range(2,n+1):
        grida[j][i]+=grida[j-1][i]
        gridt[j][i]+=gridt[j-1][i]

"""
for i in range(1,n+1):
    for j in range(1,n+1):
        print(grida[i][j],end="")
    print()
print()
for i in range(1,n+1):
    for j in range(1,n+1):
        print(gridt[i][j],end="")
    print()
"""

ans=0
for i in range(1,n+1):
    for j in range(1,n+1):
        if grida[i][j]>=1 and gridt[i][j]>=1:
            ans+=1

print(ans)