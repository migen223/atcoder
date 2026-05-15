n,k=map(int,input().split())
s=list(input())
ans=0
now=0
for i in range(n):
    if s[i]=="O":
        now+=1
        #print(now)
        if now==k:
            ans+=1
            now=0
    else:
        now=0
print(ans)
