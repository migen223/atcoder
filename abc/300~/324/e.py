from bisect import bisect_left
n,t=input().split()
n=int(n)


bl=[]
al=[]
for i in range(n):
    s=input()
    bef=[]
    aft=[]
    bi=0
    ai=1
    for j in range(len(s)):
        if 0<=bi<len(t) and s[j]==t[bi]:
            bef.append(s[j])
            bi+=1
        if 1<=ai<=len(t) and s[-j-1]==t[-ai]:
            aft.append(s[-j-1])
            ai+=1
    bl.append(len(bef))
    al.append(len(aft))

bl.sort()
al.sort()
ans=0


for i in range(n):
    ind=bisect_left(al,len(t)-bl[i])
    ans+=len(al)-ind
print(ans)
