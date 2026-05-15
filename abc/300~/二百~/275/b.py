l=list(map(int,input().split()))
for i in range(6):
    l[i]%=998244353

left=(l[0]*l[1]*l[2])
r=(l[3]*l[4]*l[5])
print((left-r)%998244353)