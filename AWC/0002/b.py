
n,m,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
td=0
num=0

for i in range(m):
    if a[b[i]-1]<k:
        td+=a[b[i]-1]
        num+=1

print(num,td)