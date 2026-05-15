
s=list(input())
orig=list("atcoder")
dic={}
for i in range(7):
    dic[orig[i]]=i

ans=0
ne=s.index("a")
ans+=abs(dic["a"]-ne)
s.remove("a")
s.insert(0,"a")

for i in range(7):
    latter=orig[i]
    ne=s.index(latter)
    ans+=abs(dic[latter]-ne)
    s.remove(latter)
    s.insert(i,latter)
print(ans)

