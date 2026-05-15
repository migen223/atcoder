
n,m=map(int,input().split())
bird=[0]*(m+1)
count=[0]*(m+1)
for i in range(n):
    a,b=map(int,input().split())
    bird[a]+=b
    count[a]+=1

for i in range(1,m+1):
    print(bird[i]/count[i])
