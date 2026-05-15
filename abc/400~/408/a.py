n,s=map(int,input().split())
i=input()
t=list(map(int,i.split()))
f=0
if t[0]>s:
    f+=1
for i in range(n-1):
    
    if t[i+1]-t[i]>s:
        f+=1
if f==0:
    print("Yes")
else:
    print("No")