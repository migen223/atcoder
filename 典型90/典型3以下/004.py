h,w=map(int,input().split())
line_sum=[]
row_sum=[]
g=[]
for a in range(h):
    i=input()
    l=list(map(int,i.split()))
    g.append(l)
for b in range(h):
    line_sum.append(sum(g[b]))
for i in range(w):
    s=0
    for j in range(h):
        s+=g[j][i]
    row_sum.append(s)
    

for d in range(h):
    for e in range(w):
        print(f"{line_sum[d]+row_sum[e]-g[d][e]} ",end="")
    print("")
