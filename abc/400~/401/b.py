n=int(input())
now=0
ans=0
for i in range(n):
    s=input()
    if s=="login":
        now=1
    elif s=="logout":
        now=0
    elif s=="private":
        if now==0:
            ans+=1

print(ans)
            
