n=int(input())
acquire=[]
skilltree=[set() for i in range(n+1)]
for i in range(n):
    a,b=map(int,input().split())
    if a==b==0:
        acquire.append(i+1)
    else:
        skilltree[a].add(i+1)
        skilltree[b].add(i+1)
acset=set()
for i in range(len(acquire)):
    acset.add(acquire[i])
while acquire:
    now=acquire.pop()
    for skill in skilltree[now]:
        if skill not in acset:
            acquire.append(skill)
            acset.add(skill)
print(len(acset))

