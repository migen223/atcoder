n=int(input())
d=list(map(int,input().split()))
ans=0
for i in range(1,n+1):
    m=str(i)
    count=0
    for j in range(len(m)):
        if m[j]==m[0]:
            count+=1
    if count==len(m):
        
        first=int(m[0])
        second=int(m[0]+m[0])
        if d[i-1]>=second:
            ans+=2
            
        elif d[i-1]>=first:
            ans+=1
print(ans)

            