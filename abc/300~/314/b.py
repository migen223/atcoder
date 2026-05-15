n=int(input())
bets=[]
betkind=[]
number=[[] for i in range(37)]
for i in range(n):
    c=int(input())
    a=list(map(int,input().split()))
    bets.append(c)
    for j in a:
        number[j-1].append(i)
x=int(input())

hits=[]
ansl=[]
hb=[]
for i in range(len(number[x-1])):
    hits.append(number[x-1][i])
for i in range(len(hits)):
    hb.append(bets[hits[i]])
for i in range(len(hb)):
    if min(hb)==hb[i]:
        ansl.append(hits[i]+1)
print(len(ansl))
print(*ansl)




