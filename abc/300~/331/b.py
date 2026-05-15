n,s,m,l=map(int,input().split())
def mod(n,size):
    worst=0
    if n%size==0:
        worst=n//size
    else:
        worst=n//size+1
    return worst
ans=999999999999
for i in range(mod(n,6)+1):
    for j in range(mod(n-6*i,8)+1):
        k=mod(n-6*i-8*j,12)
        #print(i,j,k)
        ans=min(ans,s*i+m*j+l*k)
print(ans)
