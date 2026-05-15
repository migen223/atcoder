n=int(input())
dic={}
se=set()
for i in range(n):
    a,c=map(int,input().split())
    if c in se:
        dic[c]=min(dic[c],a)
    else:
        dic[c]=a
        se.add(c)
ans=0
for taste in dic:
    ans=max(ans,dic[taste])
print(ans)