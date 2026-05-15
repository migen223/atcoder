n=int(input())
a=[]
c=[]
cardpower={}
cardind={}
for i in range(n):
    an,cn=map(int,input().split())
    a.append(an)
    c.append(cn)
    cardpower[an]=cn
    cardind[an]=i+1
ans=[]
a.sort(reverse=True)
cost=cardpower[a[0]]
for i in range(n):
    if cost>cardpower[a[i]]:
        cost=cardpower[a[i]]
        ans.append(a[i])
ans.append(a[0])
ansind=[]
for i in range(len(ans)):
    ansind.append(cardind[ans[i]])

print(len(ans))
ansind.sort()
print(*ansind)