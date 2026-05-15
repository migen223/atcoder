from itertools import permutations
m=int(input())
s1=list(input())
s2=list(input())
s3=list(input())
slot=[s1,s2,s3]
se1=set(s1)
se2=set(s2)
se3=set(s3)
ses=[se1,se2,se3]

ans=10**32
if len(se1&se2&se3)==0:
    print(-1)
else:
    for i in range(10):
        for p in permutations(range(3)):
            t=0
            f=0
            for per in p:
                if str(i) in ses[per]:
                    for k in range(m):
                        if slot[per][(t+k)%m]==str(i):
                            t+=k+1
                            break
                else:
                    f+=1
                    break
            if f==0:
                #print(i,t-1,p)
                ans=min(ans,t-1)
    print(ans)
            

