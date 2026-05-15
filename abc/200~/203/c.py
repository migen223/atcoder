
n,k=map(int,input().split())

dic={}
for i in range(n):
    a,b=map(int,input().split())
    if a not in dic:
        dic[a]=b
    else:
        dic[a]+=b

friends=[]
for i in dic:
    friends.append((i,dic[i]))

friends.sort()

ans=k
for i in range(len(friends)):
    if ans>=friends[i][0]:
        ans+=friends[i][1]
    else:
        break
print(ans)
