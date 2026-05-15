
n,s,t=map(int,input().split())
a=list(map(int,input().split()))
now=[s,0]

for i in range(n):
    if now[1]+a[i]>=60:
        now[0]+=(now[1]+a[i])//60
        now[1]=(now[1]+a[i])%60
    else:
        now[1]+=a[i]

#print(now)
if now[0]<t or (now[0]==t and now[1]==0):
    print("Yes")
else:
    print("No")