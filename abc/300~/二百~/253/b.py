h,w=map(int,input().split())
grid=[list(input()) for i in range(h)]

k=[]
for i in range(h):
    for j in range(w):
        if grid[i][j]=="o":
            k.append([i,j])
print(abs(k[0][0]-k[1][0])+abs(k[0][1]-k[1][1]))

