n=int(input())
l=list(map(int,input().split()))#0の時空いてる
visit=[0]*(n+1)
visit[0]=1
visit[n]=1

for i in range(n):
    if l[i]==0:
        visit[i+1]=1
    else:
        break
for i in range(n):
    if l[n-1-i]==0:
        visit[n-i-1]=1
    else:
        break
#print(visit)
print(n+1-sum(visit))

"""
close=[]
for i in range(len(l)):
    if l[i]==1:
        close.append(i)
if len(close)==0:
    print(n+1)
elif len(close)==1:
    print(n+1)
else:
    print(close[-1]-close[0])
"""