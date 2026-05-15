n,m=map(int,input().split())
muri=set()
for i in range(m):
    a,b=map(int,input().split())
    a-=1
    b-=1
    muri.add(tuple([a,b]))
    if a+2<=n-1 and b+1<=n-1:
        muri.add(tuple([a+2,b+1]))
    if a+2<=n-1 and b-1>=0:
        muri.add(tuple([a+2,b-1]))
    if a+1<=n-1 and b+2<=n-1:
        muri.add(tuple([a+1,b+2]))
    if a+1<=n-1 and b-2>=0:
        muri.add(tuple([a+1,b-2]))
    if a-1>=0 and b+2<=n-1:
        muri.add(tuple([a-1,b+2]))
    if a-1>=0 and b-2>=0:
        muri.add(tuple([a-1,b-2]))
    if a-2>=0 and b+1<=n-1 :
        muri.add(tuple([a-2,b+1]))
    if a-2>=0 and b-1>=0:
        muri.add(tuple([a-2,b-1]))
#print(muri)

print(n*n-len(muri))