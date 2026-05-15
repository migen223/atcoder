from collections import Counter
n=int(input())

dice=[]
p=[]

for i in range(n):
    l=list(map(int,input().split()))
    k=l.pop(0)
    c=Counter(l)
    dic={}
    for d in c:
        dic[d]=c[d]/k
    p.append(dic)
    dice.append(c)

ans=-1 
for i in range(n-1):
    for j in range(i+1,n):
        andij=dice[i]&dice[j]
        now=0
        for k in andij:
          #  print(p[i][k],p[j][k])
            now+=p[i][k]*p[j][k]
        #print(f"and={andij}")
        #print(now)
        ans=max(now,ans)
print(ans)