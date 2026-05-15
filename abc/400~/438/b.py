
n,m=map(int,input().split())
s=list(input())
t=list(input())
ans=10**32

for i in range(n-m+1):
    count=0
    tc=[str(t[i]) for i in range(m)]
    for j in range(m):
        #print(s[i+j],t[j])
        while tc[j]!=s[i+j]:
            #print("t[j]",tc[j])
            tc[j]=str((int(tc[j])+1)%10)
            count+=1
    #print(count)
    ans=min(ans,count)
print(ans)
