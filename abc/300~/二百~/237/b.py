

h,w=map(int,input().split())

grid=[list(map(int,input().split())) for i in range(h)]

ans=[[-1]*h for i in range(w)]

for i in range(h):
    for j in range(w):
        ans[j][i]=grid[i][j]

for i in range(w):
    print(*ans[i])


