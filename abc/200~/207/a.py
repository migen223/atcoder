
a,b,c=map(int,input().split())
ans=a+b
ans=max(ans,b+c)
ans=max(ans,a+c)
print(ans)