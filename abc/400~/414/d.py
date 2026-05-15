
n,m=map(int,input().split())
x=list(map(int,input().split()))

x.sort()
dic={}

diff=[x[i+1]-x[i] for i in range(n-1)]
diff.sort()

for i in range(m-1):
    if diff[-1-i] in dic:
        dic[diff[-1-i]]+=1
    else:
        dic[diff[-1-i]]=1

div=[]
now=[x[0]]
for i in range(n-1):
    if x[i+1]-x[i] in dic:
        now.append(x[i])
        div.append(now)
        now=[x[i+1]]
        dic[x[i+1]-x[i]]-=1
        if dic[x[i+1]-x[i]]==0:
            dic.pop(x[i+1]-x[i])
now.append(x[-1])
div.append(now)

ans=0
for i in range(len(div)):
    rang=div[i][1]-div[i][0]
    ans+=rang

print(ans)

