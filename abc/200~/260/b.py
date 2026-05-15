

n,x,y,z=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

math=[]
eng=[]
su=[]
for i in range(n):
    math.append((a[i],-i-1))
    eng.append((b[i],-i-1))
    su.append((a[i]+b[i],-i-1))
se=set()
math.sort(reverse=True)
eng.sort(reverse=True)
su.sort(reverse=True)
ans=[]
for i in range(x):
    ans.append(math[i][1])
    se.add(math[i][1])
k=0
for i in range(n):
    if k==y:
        break
    if eng[i][1] not in se:
        k+=1
        se.add(eng[i][1])
        ans.append(eng[i][1])
    

k=0
#print(math)
#print(eng)
#print(su)
for i in range(n):
    if k==z:
        break
    if su[i][1] not in se:
        k+=1
        se.add(su[i][1])
        ans.append(su[i][1])
    
ans.sort(reverse=True)
for i in range(len(ans)):
    print(-ans[i])
