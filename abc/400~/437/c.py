
t=int(input())

for _ in range(t):
    n=int(input())
    deer=[]
    s=0
    ans=0
    for i in range(n):
        w,p=map(int,input().split())
        deer.append((w,p))
        s+=w
    deer.sort(key=lambda x:x[1]+x[0])
    power=0
    ans=n
    #print(f"deer {deer}")
    while power<s:
        nw,np=deer.pop()
        power+=np
        s-=nw
        ans-=1
    print(ans)

    #print(f"ans={ans}")    

    
    
