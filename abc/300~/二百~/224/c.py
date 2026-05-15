from itertools import combinations
from math import gcd
n=int(input())

points=[tuple(map(int,input().split())) for i in range(n)]
ans=0

def yakubun(ue,sita):
    gc=gcd(abs(ue),abs(sita))
    return (ue//gc,sita//gc)

def minus(tu):
    return (-tu[0],-tu[1])

for p in combinations(points,3):
    m1=yakubun(p[0][1]-p[1][1],p[0][0]-p[1][0])
    m2=yakubun(p[0][1]-p[2][1],p[0][0]-p[2][0])
    if m1!=m2 and m1!=minus(m2):
        ans+=1
    
    """
    if p[0][0]==p[1][0]==p[2][0]:
        continue
    else:
        if (p[0][0]-p[1][0])*(p[0][0]-p[2][0])*(p[1][0]-p[2][0])!=0:
            m1=Fraction(p[0][1]-p[1][1],p[0][0]-p[1][0])
            m2=Fraction(p[0][1]-p[2][1],p[0][0]-p[2][0])
            c1=p[0][1]-m1*p[0][0]
            c2=p[0][1]-m2*p[0][0]
            if m1!=m2 or c1!=c2:
                ans+=1
        else:
            ans+=1
"""
    #print(p)
    #print(ans)

print(ans)
