
n,k=map(int,input().split())
c=list(map(int,input().split()))
dic={}
for i in range(k):
    if c[i] not in dic:
        dic[c[i]]=1
    else:
        dic[c[i]]+=1
ans=len(dic)
for i in range(n-k):
    dic[c[i]]-=1
    if dic[c[i]]==0:
        dic.pop(c[i])
    if c[i+k] not in dic:
        dic[c[i+k]]=1
    else:
        dic[c[i+k]]+=1
    ans=max(ans,len(dic))
print(ans)

