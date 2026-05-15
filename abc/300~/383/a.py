n=int(input())
water=0
time=0
for i in range(n):
    t,v=map(int,input().split())
    if i==0:
        water=v
        time=t
    else:
        water=max(0,water-(t-time))
        water+=v
        time=t
        #print(water)
print(water)