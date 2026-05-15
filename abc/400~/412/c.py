from bisect import bisect_right
t=int(input())


for _ in range(t):
    n=int(input())
    s=list(map(int,input().split()))
    d1=s[0]
    dn=s[-1]
    s=set(s)
    s=list(s)
    s.sort()
    ansl=[d1]
    f=0
    while 2*ansl[-1]<dn:
        ind=bisect_right(s,2*ansl[-1])-1
        if ansl[-1]==s[ind]:
            f+=1
            break
        else:
            ansl.append(s[ind])
    if f==1:
        print(-1)
    else:
        #print(ansl)
        print(len(ansl)+1)
    