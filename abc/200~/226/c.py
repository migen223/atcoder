from copy import deepcopy
n=int(input())

time=[]
require=[]
rskill=[]

for i in range(n):
    l=list(map(int,input().split()))
    time.append(l[0])
    require.append(l[1])
    rskill.append(l[2:])

ans=0

skill=[False]*n
skill[n-1]=True
need=deepcopy(rskill[n-1])
while need:
    now=need.pop()
    skill[now-1]=True
    #print(rskill[now-1])
    for i in range(len(rskill[now-1])):
        if not skill[rskill[now-1][i]-1]:
            need.append(rskill[now-1][i])
    #print(need)
for i  in range(n):
    if skill[i]:
        ans+=time[i]
#print(skill)
print(ans)
"""
need=rskill[n-1]
se=set(need)
while need:
    now=need.pop()
    ans+=time[now-1]
    for i in range(len(rskill[now-1])):
        if rskill[now-1][i] not in se:
            need.append(rskill[now-1][i])

print(time,rskill)  
         
print(ans)
  """       


