n,p,q=map(int,input().split())
an=list(map(int,input().split()))
ans=0
for a in range(n):
    for b in range(a):
        for c in range(b):
            for d in range(c):
                for e in range(d):
                    if ((an[a]%p)*(an[b]%p)*(an[c]%p)*(an[d]%p)*(an[e]%p))%p==q:
                        ans+=1
print(ans)