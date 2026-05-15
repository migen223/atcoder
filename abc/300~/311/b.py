n,d=map(int,input().split())
ans=0
ren=0
people=[]
for i in range(n):
    people.append(input())
for i in range(d):
    count=0
    for j in range(n):
        if people[j][i]=="o":
            count+=1
    if count==n:
        ren+=1
    else:
        ans=max(ans,ren)
        ren=0
ans=max(ans,ren)
print(ans)