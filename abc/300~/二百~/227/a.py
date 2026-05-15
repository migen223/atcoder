n,k,a=map(int,input().split())

now=a-1
for i in range(k-1):
    now=(now+1)%n

print(now+1)

