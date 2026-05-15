n=int(input())
p=list(map(int,input().split()))
r=1
people=[-1]*n
while -1 in people:
    ma=max(p)
    count=0
    for j in range(n):
        if p[j]==ma:
            p[j]=-1
            people[j]=r
            count+=1
    r+=count

for i in range(n):
    print(people[i])