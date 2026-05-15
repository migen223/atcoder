from collections import Counter
s=input()
mod=998244353
n=len(s)
ans=0
dp=[[0 for _ in range(n)] for _ in range(3)]
dic={"a":0,"b":1,"c":2}
dp[dic[s[0]]][0]=1
for i in range(1,n):
    for j in range(3):
        dp[j][i]+=dp[j][i-1]
        if dic[s[i]]!=j:
            dp[dic[s[i]]][i]+=dp[j][i-1]
        dp[j][i]%=mod
    dp[dic[s[i]]][i]+=1
    dp[dic[s[i]]][i]%=mod
    
    #for i in range(3):
     #   print(*dp[i])
    #print()

for i in range(3):
    ans+=dp[i][-1]
print(ans%mod)

"""
ans=n
fact=[1,1]
for i in range(2,10**5+1):
    fact.append((fact[-1]*i)%mod)
rfact=[pow(fact[i],-1,mod) for i in range(len(fact))]


c=Counter(s)
l=["a","b","c"]
for i in range(3):
    if l[i] not in c:
        c[l[i]]=0

a=0
b=0
cn=0
for i in range(1,1+c["a"]):
    a+=fact[c["a"]]*rfact[i]*rfact[c["a"]-i]
    a%=mod
for i in range(1,1+c["b"]):
    b+=fact[c["b"]]*rfact[i]*rfact[c["b"]-i]
    b%=mod
for i in range(1,1+c["c"]):
    cn+=fact[c["c"]]*rfact[i]*rfact[c["c"]-i]
    cn%=mod
ans+=a*b
ans%=mod
ans+=b*cn
ans%=mod
ans+=a*cn
ans%=mod
ans+=a*b*cn
ans%=mod
print(a,b,cn)

print(ans)"""