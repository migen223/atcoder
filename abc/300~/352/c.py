n=int(input())
shoulder=[]
head=[]

for i in range(n):
    a,b=map(int,input().split())
    shoulder.append(a)
    head.append(b)
"""
ans=0
s=sum(shoulder)
for i in range(n):
    ans=max(ans,s-shoulder[i]+head[i])
print(ans)
"""
ma=-1
maind=0
for i in range(n):
    if head[i]-shoulder[i]>ma:
        ma=head[i]-shoulder[i]
        maind=i
print(sum(shoulder)-shoulder[maind]+head[maind])
