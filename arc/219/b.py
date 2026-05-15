from itertools import permutations
from collections import Counter
t=int(input())
mod=998244353

def change(l):
    res=[]
    rev=[]
    nor=[]
    f=0
    f2=0
   # print("l",l)
    for i in range(n):
       # print("res in",res)
        if f==0:
            if i+1!=l[i]:
                f+=1
                top=i+1
                rev.append(l[i])
            else:
                res.append(l[i])
        else:
            if f2==0:
                if l[i]==top:
                    rev.append(l[i])
                    while rev:
                        res.append(rev.pop())
                    f2+=1
                else:
                    rev.append(l[i])
            else:
                res.append(l[i])
    return res


for _ in range(t):
    n=int(input())
    p=list(map(int,input().split()))
    if n==1:
        print(1)
        continue
    """
    ans=[]
    for per in permutations(range(1,n+1)):
        res=change(per)
        #print("res",per,res)

        ans.append(tuple(res))
        
    #print(ans)
    print(Counter(ans))"""
    ans=0
    for i in range(n):
        if i+1==p[i]:
            ans+=n-(i+1)
            ans%=mod
        else:
            break
    if p==list(range(1,n+1)):
        ans+=1
        ans%=mod
    print(ans)

            
        



"""
(1, 2, 3, 4) 
(1, 2, 4, 3) 1234
(1, 3, 2, 4)1234
(1, 3, 4, 2)1243
(1, 4, 2, 3)1243
(1, 4, 3, 2)1234
(2, 1, 3, 4)1234
(2, 1, 4, 3)1243
(2, 3, 1, 4)1324
(2, 3, 4, 1)1432
(2, 4, 1, 3)1423
(2, 4, 3, 1)
(3, 1, 2, 4)
(3, 1, 4, 2)
(3, 2, 1, 4)
(3, 2, 4, 1)
(3, 4, 1, 2)
(3, 4, 2, 1)
(4, 1, 2, 3)
(4, 1, 3, 2)
(4, 2, 1, 3)
(4, 2, 3, 1)
(4, 3, 1, 2)
(4, 3, 2, 1)
"""