
n=int(input())
q=int(input())
box=[[] for i in range(n+1)]
boxflag=[True]*(n+1)
cs=set()
cd={}
cdf={}
cdfs={}

for i in range(q):
    que=input().split()
    #print(cd,cs)
    #print(box)
    #print(cdfs)
    if que[0]=="1":
        c=int(que[1])
        b=int(que[2])
        if c in cs:
            if b not in cdfs[c]:
                cd[c].append(b)
                cdf[c]=False
                cdfs[c].add(b)
        else:
            cs.add(c)
            cd[c]=[b]
            cdf[c]=True
            cdfs[c]=set()
            cdfs[c].add(b)
        box[b].append(c)
        boxflag[b]=False

    if que[0]=="2":
        b=int(que[1])
        if not boxflag[b]:
            box[b].sort()
            boxflag[b]=True
        print(*box[b])
    if que[0]=="3":
        c=int(que[1])
        s=set()
        if not cdf[c]:
            cd[c].sort()
            cdf[c]=True
        print(*cd[c])

