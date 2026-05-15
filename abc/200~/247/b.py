import sys

n=int(input())
se=set()
people=[]
for i in range(n):
    name=input().split()
    people.append(name)

for i in range(n):
    count=0
    for j in range(2):
        for k in range(n):
            if i!=k:
                if people[i][j] in people[k]:
                    count+=1
                    break
    if count==2:
        print("No")
        sys.exit()
print("Yes")
