
n,k=map(int,input().split())
a=list(map(int,input().split()))
dic={}
s=sum(a)
for i in range(n):
    if a[i] not in dic:
        dic[a[i]]=a[i]
    else:
        dic[a[i]]+=a[i]

l=[]
for i in dic:
    l.append(dic[i])
l.sort()
sub=0
if len(l)>=k:
    for i in range(k):
        sub+=l.pop()
else:
    sub=sum(l)
print(s-sub)