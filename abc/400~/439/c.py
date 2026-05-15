from math import sqrt
n=int(input())

ans={}

x=1
while x**2<=n:
    y=x+1
    while x**2+y**2<=n:
        if x**2+y**2 in ans:
            ans[x**2+y**2]+=1
        else:
            ans[x**2+y**2]=1
        y+=1
    x+=1
    
ansl=[]
for i in ans:
    if ans[i]==1:
        ansl.append(i)
ansl.sort()
print(len(ansl))
print(*ansl)


