n,a=map(int,input().split())
t=list(map(int,input().split()))
time=t[0]+a
print(time)
for i in range(1,n):
    if time>=t[i]:
        print(time+a)
        time+=a
    else:
        print(t[i]+a)
        time=t[i]+a