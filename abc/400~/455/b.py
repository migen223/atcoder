
h,w=map(int,input().split())

grid=[input() for i in range(h)]

ans=0

for h1 in range(h):
    for h2 in range(h1,h):
        for w1 in range(w):
            for w2 in range(w1,w):
                f=0
                for i in range(h1,h2+1):
                    for j in range(w1,w2+1):
                        if grid[i][j]!=grid[h1+h2-i][w1+w2-j]:
                            f+=1
                        if f!=0:
                            break
                    if f!=0:
                        break
                if f==0:
                    ans+=1

print(ans)