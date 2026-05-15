
h,w,n=map(int,input().split())

choc=[]
height={}
width={}
for i in range(n):
    hi,wi=map(int,input().split())
    if hi in height:
        height[hi].append((hi,wi,i))
    else:
        height[hi]=[(hi,wi,i)]
    if wi in width:
        width[wi].append((hi,wi,i))
    else:
        width[wi]=[(hi,wi,i)]
    choc.append((hi,wi,i))

ans=[[-1,-1] for i in range(n)]
ban=set()
while h>0 and w>0:
    if h in height:
        for c in height[h]:
            hi,wi,i=c
            if (hi,wi,i) in ban:
                continue
            w-=wi
            ans[i]=[1,w+1]
            ban.add((hi,wi,i))
    #print("h",h,w,hi,wi,i)

    if w in width:
        for c in width[w]:
            hi,wi,i=c
            if (hi,wi,i) in ban:
                continue
            h-=hi
            ans[i]=[h+1,1]
            ban.add((hi,wi,i))
    #print("w",h,w,hi,wi,i)


for i in range(n):
    print(*ans[i])