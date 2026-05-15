from collections import Counter
n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))

ans=0

cc=Counter(c)
dic={}
for mc in cc.most_common():
    if b[mc[0]-1] in dic:
        dic[b[mc[0]-1]]+=mc[1]
    else:
        dic[b[mc[0]-1]]=mc[1]

for i in range(n):
    if a[i] in dic:
        ans+=dic[a[i]]
print(ans)
