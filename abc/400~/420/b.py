n,m=map(int,input().split())
ans=[0]*n
result=[]
for i in range(n):
    s=input()
    result.append(s)
for i in range(m):
    c1=0
    c0=0
    for j in range(n):
        if result[j][i]=="1":
            c1+=1
        else:
            c0+=1
    if c1*c0==0:
        for k in range(n):
            ans[k]+=1
    elif c1>c0:
        for j in range(n):
            if result[j][i]=="0":
                ans[j]+=1
    else:
        for j in range(n):
            if result[j][i]=="1":
                ans[j]+=1
ma=max(ans)
for i in range(n):
    if ans[i]==ma:
        print(i+1,end=" ")
print()