from math import gcd
from collections import Counter
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort(key=lambda x:abs(x))
    se=set(a)
    abset=set([abs(a[i]) for i in range(n)])
    if len(abset)>1:
        c=Counter(a)
        gc=gcd(abs(a[0]),abs(a[1]))
        f=0
        ansl=[]
        if a[0]*a[1]<0:
            r=(abs(a[0])//gc,-abs(a[1])//gc)
        else:
            r=(abs(a[0])//gc,abs(a[1])//gc) #分母、分子
        #print("R",r)
        for i in range(n):
            #print((a[0]*((r[1]**i)))//(r[0]**i),"an")
            if (a[0]*(r[1]**i))%(r[0]**i)==0:
                ansl.append((a[0]*(r[1]**i))//(r[0]**i))
                """
                if (a[0]*(r[1]**i))//(r[0]**i) not in se:
                    f+=1
                    #print((a[0]*(a[i]*(r[1]**i)))//(r[0]**i),"ifebla")
                    break"""
            else:
                f+=1
                break
        
        if f==0:
            if c==Counter(ansl):
                print("Yes")
            else:
                print("No")
        else:
            print("No")
    else:
        if len(se)==1:
            print("Yes")
        else:

            plus=0
            minus=0
            for i in range(n):
                if a[0]!=a[i]:
                    plus+=1
                else:
                    minus+=1
            if (abs(plus-minus))<=1:
                print("Yes")
            else:
                print("No")
