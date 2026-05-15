n,m=map(int,input().split())
s=list(input())
c=list(map(int,input().split()))
color=[[] for i in range(m)]
for i in range(n):
    color[c[i]-1].append(s[i])
c_ind=[]
for i in range(m):
    c_ind.append(len(color[i])-1)

ans=""
for i in range(n):
    ans+=color[c[i]-1][(c_ind[c[i]-1])%len(color[c[i]-1])]
    c_ind[c[i]-1]+=1
print(ans)