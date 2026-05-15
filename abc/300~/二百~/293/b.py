n=int(input())
a=list(map(int,input().split()))
people=[0]*(n+1)
ans=[]
for i in range(1,n+1):

    if people[i]==0:
        people[a[i-1]]=1
    #print(people)
    
ans=[]
for i in range(1,n+1):
    if people[i]==0:
        ans.append(i)
print(len(ans))
print(*ans)


