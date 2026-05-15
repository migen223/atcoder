n=int(input())
h=list(map(int,input().split()))
t=0
def attack(h,t):
    base=h//5
    mod=h%5
    if mod==0:
        return 3*base
    elif mod==1:
        return 3*base+1
    elif mod==2:
        if t==0 or t==1:
            return 3*base+2
        else:
            return 3*base+1
    elif mod==3:
        if t==0:
            return 3*base+3
        elif t==1:
            return 3*base+2
        else:
            return 3*base+1
    elif mod==4:
        if t==0:
            return 3*base+3
        else:
            return 3*base+2
for i in range(n):
    t+=attack(h[i],t%3)
print(t)