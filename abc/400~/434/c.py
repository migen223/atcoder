
q=int(input())

for _ in range(q):
    n,h=map(int,input().split())
    now=[h,h]
    nt=0
    f=0
    for i in range(n):
        t,l,u=map(int,input().split())
        dt=t-nt
        now=[now[0]-dt,now[1]+dt]
        #print(now)
        if u<now[0] or l>now[1]:
            f+=1
        else:
            #print(f"0,l {now[0]} と{l}")
            #print(f"1,u {now[1]}と{u}")
            now[0]=max(now[0],l)
            now[1]=min(now[1],u)
        nt=t
        #print(f"nt={nt}")
        #print(now)
    if f==0:
        print("Yes")
    else:
        print("No")


     