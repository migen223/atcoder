
s=input()
n=len(s)


now=[0]*10
dic={}
dic[tuple(now)]=1
for i in s:
    now[int(i)]=(now[int(i)]+1)%2
    ns=tuple(now)
    if ns in dic:
        dic[ns]+=1
    else:
        dic[ns]=1
ans=0
for i in dic:
    ans+=(dic[i]*(dic[i]-1))//2
print(ans)