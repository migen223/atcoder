import sys
from math import isqrt
n=int(input())

def issqrt(n):
    sq=isqrt(n)
    if sq**2==n:
       return sq
    return -1

k=1
while (k**3)-3*(k**2)+3*k<=n:
    #print(k)
    r=9*(k**4)-12*k*(k**3-n)
    sq=issqrt(r)
    #print(r,sq)
    if r>0 and sq!=-1:
        plus=3*(k**2)+sq
        minus=3*(k**2)-sq
        #print(plus,minus)
        if minus>0 and minus%(6*k)==0 and minus//(6*k)>k:
            print(minus//(6*k),minus//(6*k)-k)
            sys.exit()
        if plus%(6*k)==0 and plus//(6*k)>k:
            print(plus//(6*k),plus//(6*k)-k)
            sys.exit()
    k+=1

print(-1)