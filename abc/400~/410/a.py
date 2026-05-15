n=int(input())
i=input()
l=list(map(int,i.split()))
k=int(input())
ans=0
for i in range(len(l)):
    if k<=l[i]:
        ans+=1
print(ans)