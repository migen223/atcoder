from math import gcd
a,b,c=map(int,input().split())
cube=[a,b,c]
g=gcd(a,b,c)
ans=0
for a in cube:
    ans+=a//g-1
print(ans)

        
