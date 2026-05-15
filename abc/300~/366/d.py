n=int(input())

l3=[[] for i in range(n)]
for i in range(n):
    for j in range(n):
        l2=list(map(int,input().split()))

        l3[i].append(l2)

       
for i in range(n):
    for j in range(n):
        for k in range(1,n):
            l3[i][j][k]+=l3[i][j][k-1]
#print(l3)
for i in range(n):
    for j in range(n):
        for k in range(1,n):
            l3[i][k][j]+=l3[i][k-1][j]
#print(l3)
for i in range(n):
    for j in range(n):
        for k in range(1,n):
            l3[k][i][j]+=l3[k-1][i][j]
#print(l3)
q=int(input())

for i in range(q):
    lr=list(map(int,input().split()))
    nq=list(map(lambda x:x-1 ,lr))
    ans=l3[nq[1]][nq[3]][nq[5]]
    if nq[0]!=0:
        ans-=l3[nq[0]-1][nq[3]][nq[5]]
    if nq[2]!=0:
        ans-=l3[nq[1]][nq[2]-1][nq[5]]
    if nq[4]!=0:
        ans-=l3[nq[1]][nq[3]][nq[4]-1]
    if nq[0]!=0 and nq[4]!=0:
        ans+=l3[nq[0]-1][nq[3]][nq[4]-1]
    if nq[0]!=0 and nq[2]!=0:
        ans+=l3[nq[0]-1][nq[2]-1][nq[5]]
    if nq[2]!=0 and nq[4]!=0:
        ans+=l3[nq[1]][nq[2]-1][nq[4]-1]
    if nq[0]!=0 and nq[2]!=0 and nq[4]!=0:
        ans-=l3[nq[0]-1][nq[2]-1][nq[4]-1]
    print(ans)    



