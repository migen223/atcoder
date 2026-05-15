from collections import Counter
n,d=map(int,input().split())
a=list(map(int,input().split()))

co=Counter(a)
used=set()
ans=0
if d!=0:
    for c in co:
        if c not in used:
            res=[(c,co[c])]
            used.add(c)
            visitable=[c]
            while visitable:
                now=visitable.pop()
                ne=now+d
                pre=now-d
                if ne in co and ne not in used:
                    used.add(ne)
                    visitable.append(ne)
                    res.append((ne,co[ne]))
                if pre in co and pre not in used:
                    used.add(pre)
                    visitable.append(pre)
                    res.append((pre,co[pre]))
            res.sort(key=lambda x:x[0])
            resn=[res[i][1] for i in range(len(res))]
            dp=[[0]*len(res) for i in range(2)]
            dp[0][0]=resn[0]
            for i in range(len(res)-1):
                dp[1][i+1]=max(dp[1][i+1],dp[0][i],dp[1][i])
                dp[0][i+1]=max(dp[0][i+1],dp[1][i]+resn[i+1])
            ans+=sum(resn)-(max(dp[0][-1],dp[1][-1]))
else:
    ans=n-len(co)

print(ans)