n,m=map(int,input().split())
goods=list(map(int,input().split()))
if sum(goods)<=m:
    print("Yes")
else:
    print("No")
