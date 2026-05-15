n,s,d=map(int ,input().split())
f=0
for _ in range(n):
    x,y=map(int,input().split())
    if x>=s or y<=d:
        continue
    else:
        f+=1
if f==0:
    print("No")
else:
    print("Yes")