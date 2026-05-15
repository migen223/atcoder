
h,w=map(int,input().split())
grid=[list(map(int,input().split())) for i in range(h)]
ans=[[] for i in range(h)]
dic={}
for i in range(65,91):
    dic[i-64]=chr(i)
for i in range(h):
    for j in range(w):
        if grid[i][j]==0:
            ans[i].append(".")
        else:
            ans[i].append(dic[grid[i][j]])
for i in range(h):
    print("".join(ans[i]))