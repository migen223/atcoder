import sys
h,w=map(int,input().split())
s=0
a=[]
b=[]
ans=0
f1=0
for _ in range(h):
    a.append(list(map(int,input().split())))
for _ in range(h):
    b.append(list(map(int,input().split())))
for i in range(h-1):
    for j in range(w-1):
        if a[i][j]!=b[i][j]:
            dif=b[i][j]-a[i][j]
            a[i][j]+=dif
            a[i][j+1]+=dif
            a[i+1][j]+=dif
            a[i+1][j+1]+=dif
            ans+=abs(dif)
    if a[i][w-1]!=b[i][w-1]:
        print("No")
        f1+=1
        sys.exit()
f=0
for i in range(w):
    if a[h-1][i]!=b[h-1][i]:
        f+=1

if f==0:
    print("Yes")
    print(ans) 
else:
    print("No")       
    
