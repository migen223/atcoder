
d,f=map(int,input().split())
ans=0
now=f
while now<=d:
    now+=7
    ans+=1
print(now-d)