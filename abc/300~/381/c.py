n=int(input())
s=list(input())
ans=1
bs=[]
for i in range(n):
    if s[i]=="/":
        bs.append(i)
for i in range(len(bs)):
    k=1
    while bs[i]-k>=0 and bs[i]+k<=n-1:
        if s[bs[i]-k]=="1" and s[bs[i]+k]=="2":
            k+=1
        else:
            break
    ans=max(ans,1+2*(k-1))
print(ans)
        