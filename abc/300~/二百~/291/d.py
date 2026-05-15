
n=int(input())

dp1=[0]*n
dp2=[0]*n
dp1[0]=1
dp2[0]=1
card=[]
p=998244353 
for i in range(n):
    a,b=map(int,input().split())
    card.append((a,b))

for i in range(n-1):
    if card[i][0]!=card[i+1][0]:
        dp1[i+1]+=dp1[i]
        dp1[i+1]%=p
    if card[i][0]!=card[i+1][1]:
        dp2[i+1]+=dp1[i]
        dp2[i+1]%=p
    if card[i][1]!=card[i+1][0]:
        dp1[i+1]+=dp2[i]
        dp1[i+1]%=p
    if card[i][1]!=card[i+1][1]:
        dp2[i+1]+=dp2[i]
        dp2[i+1]%=p

print((dp1[-1]+dp2[-1])%p)

