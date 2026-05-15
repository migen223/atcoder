
h,w=map(int,input().split())
ans=[[] for i in range(h)]

for i in range(h):
    for j in range(w):
        if i==h-1 or i==0:
            ans[i].append("#")
        else:
            if j==0 or j==w-1:
                ans[i].append("#")
            else:
                ans[i].append(".")

for i in range(h):
    for j in range(w):
        print(ans[i][j],end="")
    print()