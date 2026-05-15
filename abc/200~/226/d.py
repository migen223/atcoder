from math import gcd
n=int(input())

towns=[]
se=set()
for i in range(n):
    x,y=map(int,input().split())
    towns.append((x,y))

for i in range(n-1):
    for j in range(i+1,n):
        x1=towns[i][0]
        y1=towns[i][1]
        x2=towns[j][0]
        y2=towns[j][1]
        a=x1-x2
        b=y1-y2
        g=gcd(abs(a),abs(b))
        a//=g
        b//=g
        if (-a,-b) not in se:
            se.add((a,b))
print(len(se)*2)
