
s=input()
ans=0
n=len(s)
for i in range(n):
    for j in range(i,n):
        f=0
        for k in range(j+1-i):
            if s[i+k]!=s[j-k]:
                f+=1
        if f==0:
            ans=max(ans,j-i+1)
print(ans)