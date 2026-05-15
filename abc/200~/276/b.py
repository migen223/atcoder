n,m=map(int,input().split())
town=[]
#各町が繋がってるまちの集合
for i in range(n):
    town.append([])
for j in range(m):
    a,b=map(int,input().split())
    town[a-1].append(b)
    town[b-1].append(a)

for i in range(n):
    town[i].sort()
    print(f"{len(town[i])} ",end="")
    print(*town[i])