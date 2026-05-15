
n=int(input())
slot=[input() for i in range(n)]
numbers=[[] for i in range(10)]


for i in range(10):
    for j in range(n):
        for k in range(10):
            if int(slot[j][k])==i:
                numbers[i].append(k)

#print(numbers)
ans=10**18
for i in range(10):
    now=0
    count=0
    l=[]
    se=set()
    dic={}
    #print(*numbers[i])
    for j in range(n):
        #print(dic)
        if numbers[i][j] not in se:
            se.add(numbers[i][j])
            dic[numbers[i][j]]=1
            l.append(numbers[i][j])
        else:
            l.append(numbers[i][j]+10*dic[numbers[i][j]])
            dic[numbers[i][j]]+=1
    now=max(l)
    ans=min(ans,now)
print(ans)
        