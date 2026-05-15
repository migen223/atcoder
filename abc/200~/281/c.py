n,t=map(int,input().split())
a=list(map(int,input().split()))

total=sum(a)
roop=t//total
t-=total*roop

time=0
for i in range(n):
    if t-a[i]<=0:
        print(i+1,end=" ")
        print(t)
        break
    else:
        t-=a[i]

