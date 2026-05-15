#bitDP https://atcoder.jp/contests/abc318/tasks/abc318_d
n=0
dp=[-1]*(2**n)
edge={}
for i in range(2**n):
    if dp[i]!=-10**6:
        for j in range(n):
            if not (i>>j)&1:#(i>>j)&1 →j bit目がたっているかどうか
                for k in range(j+1,n):
                    if not (i>>k)&1:
                        next=i|(1<<j)|(1<<k) #i|(1<<j) →iのjbit目を立たせる
                        dp[next]=max(dp[next],dp[i]+edge[(j,k)])
                        ans=max(ans,dp[next])