
n,m=map(int,input().split())

home=[0]*(n+1)

for i in range(m):
    a,b=input().split()
    a=int(a)
    if home[a]==0 and b=="M":
        print("Yes")
        home[a]+=1
    else:
        print("No")