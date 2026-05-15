n=int(input())
grida=[]
gridb=[]
for i in range(n):
    grida.append(list(input()))
for i in range(n):
    gridb.append(list(input()))
ans=[0,0]
for i in range(n):
    for j in range(n):
        if grida[i][j]!=gridb[i][j]:
            ans[0],ans[1]=i+1,j+1
print(*ans)