
n,q=map(int,input().split())
x=list(map(lambda x:int(x)-1,input().split()))

num=[[] for _ in range(n)]
setl=[]
se=set()

for i in range(q):
    if x[i] in se:
        se.discard(x[i])
    else:
        se.add(x[i])
    num[x[i]].append(i)
    setl.append(len(se))

r=[0]
for i in range(len(setl)):
    r.append(r[-1]+setl[i])
#print(*setl)

for i in range(n):
    if len(num[i])%2!=0:
        num[i].append(-1)
#print(num)
#print(r)

ans=[0]*n
for i in range(n):
    for j in range(len(num[i])//2):
        ans[i]+=r[num[i][2*j+1]]-r[num[i][2*j]]
        #print(num[i][2*j+1],num[i][2*j])

print(*ans)
