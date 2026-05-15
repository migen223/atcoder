import heapq
n,k=map(int,input().split())
a=list(map(int,input().split()))
hq=list(set(a))
hq=list(map(lambda x:-x,hq))
heapq.heapify(hq)
m=max(a)
dic={}

for i in range(n):
    if a[i] in dic:
        dic[a[i]].add(i)
    else:
        dic[a[i]]=set([i])
ansl=[m]*n
vis=[-1]*n
while hq:
    now=-heapq.heappop(hq)
    l=dic[now]
    for ne in l:
        vis[ne]=now
        pre=ne-1
        aft=ne+1
        if 0<=pre<=n-1 :
            if vis[pre]==-1:
                if a[pre]<now-k:
                    if hq[0]!=k-now:
                        heapq.heappush(hq,k-now)
                    dic[a[pre]].discard(pre)
                    vis[pre]=now-k
                    if now-k in dic:
                        dic[now-k].add(pre)
                    else:
                        dic[now-k]=set([pre])
                else:
                    vis[pre]=a[pre]
        if 0<=aft<=n-1 :
            if vis[aft]==-1:
                if a[aft]<now-k:
                    if hq[0]!=k-now:
                        heapq.heappush(hq,k-now)
                    dic[a[aft]].discard(aft)
                    vis[aft]=now-k
                    if now-k in dic:
                        dic[now-k].add(aft)
                    else:
                        dic[now-k]=set([aft])
                else:
                    vis[aft]=a[i]
    ##print("vis",vis)
    #print("hq",hq)
    #print("dic",dic)
                
ans=0
for i in range(n):
    ans+=abs(abs(a[i]-vis[i]))
print(ans)