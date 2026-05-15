n=int(input())
people=[0]*n
hyou=[]
vics=[[] for i in range(101)]
for i in range(n):
    hyou.append(input())
for i in range(n):
    for j in range(n):
        if hyou[i][j]=="o":
            people[i]+=1
ans=[]
for i in range(n):
    vics[people[i]].append(i+1)
#print(vics)
for i in range(100,-1,-1):
    for j in range(len(vics[i])):
        ans.append(vics[i][j])
print(*ans)