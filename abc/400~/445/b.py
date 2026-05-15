
n=int(input())

ss=[]
for i in range(n):
    s=list(input())
    ss.append(s)

ma=0
for i in range(n):
    ma=max(ma,len(ss[i]))

for i in range(n):
    ans=["."]*ma
    gap=(ma-len(ss[i]))//2
    for j in range(len(ss[i])):
        ans[j+gap]=ss[i][j]
    print("".join(ans))