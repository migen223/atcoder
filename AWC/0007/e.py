def toyx(num):
    return [num//n,num%n]

def count(p1,p2):
    return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])

n,m=map(int,input().split())
s,t=map(lambda x:int(x)-1,input().split())


if m!=0:
    p=list(map(lambda x:int(x)-1,input().split()))
    pyx=[toyx(p[i]) for i in range(m)]
    pyx.insert(0,toyx(s))
    ans=10**32
    dp=[[10**32]*(2**m) for i in range(m+1)]
    
    dp[0][0]=0
    for i in range(2**m):
        for j in range(m+1): #最終地点の座標へのポインタ(y,x)
            if dp[j][i]!=10**32:
                for k in range(m): #たたせるbit
                    if not (i>>k)&1:#(i>>j)&1 →j bit目がたっているかどうか
                        next=i|(1<<k)
                        #print(next)
                        dp[k+1][next]=min(dp[k+1][next],dp[j][i]+count(pyx[j],pyx[k+1]))
    
    #for i in range(m+1):
     #   print(*dp[i])

    for i in range(1,m+1):
        ans=min(ans,dp[i][-1]+count(pyx[i],toyx(t)))
    print(ans)
else:
    print(count(toyx(s),toyx(t)))