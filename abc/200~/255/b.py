from math import sqrt
n,k=map(int,input().split())
a=list(map(int,input().split()))

people=[]
for i in range(n):
    p=list(map(int,input().split()))
    people.append(p)

light=[]
lights=set(a)

for i in range(k):
    light.append(people[a[i]-1])

need=[]
for i in range(n):
    if i+1 not in lights:
        now=10**18
        for j in range(k):
            now=min(now,sqrt(((people[i][0]-light[j][0])**2+(people[i][1]-light[j][1])**2)))
        need.append(now)
print(max(need))
        


