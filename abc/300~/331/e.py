
n,m,l=map(int,input().split())


a=list(map(int,input().split()))
b=list(map(int,input().split()))

dic={}
for _ in range(l):
    c,d=map(lambda x:int(x)-1,input().split())
    if c in dic:
        dic[c].append(b[d])
    else:
        dic[c]=[b[d]]
for i in dic:
    dic[i].sort(reverse=True)
ans=0
b.sort(reverse=True)

for i in range(n):
    if i in dic:
        f=0
        for j in range(len(dic[i])):
            if b[j]!=dic[i][j]:
                ans=max(ans,a[i]+b[j])
                f+=1
                break
        if f==0 and 0<=j+1<=m-1:
            ans=max(ans,a[i]+b[j+1])
        
    else:
        ans=max(ans,a[i]+b[0])
print(ans)
