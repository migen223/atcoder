
n,k=map(int,input().split())
a=list(map(int,input().split()))
ruiseki=[0]

for i in range(n):
    ruiseki.append(ruiseki[-1]+a[i])

dic={0:1}
ans=0

for i in range(1,n+1):
    need=ruiseki[i]-k

    if need in dic:
        ans+=dic[need]
    if ruiseki[i] not in dic:
        dic[ruiseki[i]]=1
    else:
        dic[ruiseki[i]]+=1
    
print(ans)

