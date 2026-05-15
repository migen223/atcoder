
t=input()
n=int(input())

dp=[[10**5]*len(t) for i in range(n)]

bags=[]
for i in range(n):
    l=input().split()
    a=int(l[0])
    s=l[1:]
    bag=[]
    for j in s:
        if len(j)<=len(t):
            for k in range(len(t)-len(j)+1):
                li=[]
                for l in range(len(j)):
                    if j[l]==t[k+l]:
                        li.append(k+l)
                if len(li)==len(j):
                    bag.append((li[0],li[-1]))
    bags.append(bag)

#print(bags)
for i in range(len(bags[0])):
    if bags[0][i][0]==0:
        dp[0][bags[0][i][1]]=1

for i in range(1,n):
    for str in bags[i]:
        if str[0]==0:
            dp[i][str[1]]=1
        if dp[i-1][str[0]-1]!= 10**5:
            dp[i][str[1]]=min(dp[i-1][str[0]-1]+1,dp[i][str[1]])
    for j in range(len(t)):
        dp[i][j]=min(dp[i][j],dp[i-1][j])

"""
for i in range(n):
    print(*dp[i])
"""
    
if dp[-1][-1]==10**5:
    print(-1)
else:
    print(dp[-1][-1])



