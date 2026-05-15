
r=int(input())
ans=1+(r-1)*4

now=r
for i in range(1+1,r+1):
    #print((now-0.5)**2+(i-0.5)**2<=r**2)
    if (now-0.5)**2+(i-0.5)**2<=r**2:
        ans+=(now-1)*4
    else:
        while (now-0.5)**2+(i-0.5)**2>r**2:
            now-=1
        ans+=(now-1)*4
print(ans)
