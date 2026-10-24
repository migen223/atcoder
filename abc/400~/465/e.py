import sys

def debug(*x):print('debug:',*x, file=sys.stderr)
sys.setrecursionlimit(300000)
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 61 - 1
mod = 998244353
#mod=10**9+7
dy=[-1,1,0,0]
dx=[0,0,-1,1]
#dy=[-1,-1,-1,1,1,1,0,0]
#dx=[-1,0,1,-1,0,1,-1,1]
"""
i|(1<<j) →iのjbit目を立たせる
(i>>j)&1 →j bit目がたっているかどうか
"""
s=input()
n=len(s)
ni=[int(s[i]) for i in range(n)]

dp=[[[[[0 for _ in range(2**10)] for _ in range(3)] for _ in range(2)] for _ in range(2)] for _ in range(n)]
#桁、以下、start,mod 3 ,何を使ったか

for i in range(1,10):
    if i<ni[0]:
        dp[0][1][1][i%3][0|(1<<i)]+=1
    elif i==ni[0]:
        dp[0][0][1][i%3][0|(1<<i)]+=1
        break
dp[0][1][0][0][0]+=1



for i in range(n-1):
    for j in range(2):
        for k in range(2):
            for l in range(3):
                for m in range(2**10):
                    if dp[i][j][k][l][m]>=1:
                        if j==1:
                            if k==1:
                                for p in range(10):
                                    dp[i+1][j][k][(l+p)%3][m|(1<<p)]+=dp[i][j][k][l][m]
                                    dp[i+1][j][k][(l+p)%3][m|(1<<p)]%=mod
                            else:
                                for p in range(1,10):
                                    dp[i+1][j][1][(l+p)%3][m|(1<<p)]+=dp[i][j][k][l][m]
                                    dp[i+1][j][1][(l+p)%3][m|(1<<p)]%=mod
                                dp[i+1][j][0][l][m]+=dp[i][j][k][l][m]
                                dp[i+1][j][0][l][m]%=mod
                        else: #(j=0) k=1 が確定してる
                            #if k==1:
                            for p in range(ni[i+1]):
                                dp[i+1][1][k][(l+p)%3][m|(1<<p)]+=dp[i][j][k][l][m]
                                dp[i+1][1][k][(l+p)%3][m|(1<<p)]%=mod
                            dp[i+1][0][k][(l+ni[i+1])%3][m|(1<<ni[i+1])]+=dp[i][j][k][l][m]
                            dp[i+1][0][k][(l+ni[i+1])%3][m|(1<<ni[i+1])]%=mod
                            """
                            else:
                                debug("おかしい")
                                for p in range(1,ni[i+1]):
                                    dp[i+1][1][1][(l+p)%3][m|(1<<p)]+=dp[i][j][k][l][m]
                                    dp[i+1][1][1][(l+p)%3][m|(1<<p)]%=mod
                                dp[i+1][j][0][l][m]+=dp[i][j][k][l][m]
                                dp[i+1][j][0][l][m]%=mod
                                dp[i+1][0][k][((l+ni[i+1])%3)][m|(1<<ni[i+1])]+=dp[i][j][k][l][m]
                                dp[i+1][0][k][((l+ni[i+1])%3)][m|(1<<ni[i+1])]%=mod"""
                            
ans=0

for j in range(2):
    for k in range(3):
        for l in range(2**10):
            f=0
            if k==0:
                f+=1
            if (l>>3)&1 :
                f+=1
            count=0
            for ii in range(10):
                if (l>>ii)&1 :
                    count+=1
            if count==3:
                f+=1
            if f==1:
                
                ans+=dp[-1][j][1][k][l]
                ans%=mod 
print(ans)
    

    