
s=list(input())
k=int(input())

l=0
r=0
count=0
now=0
ans=0

if k!=0:
    while r<len(s) and l<=r:
        if s[r]=="X":
            r+=1
            now+=1
            ans=max(ans,now)
        else:
            if count+1>k:
                if s[l]==".":
                    count-=1
                l+=1
                now-=1
            else:
                count+=1
                now+=1
                r+=1
                ans=max(ans,now)

    print(ans)

else:
    ans=0
    now=0
    for i in range(len(s)):
        if s[i]=="X":
            now+=1
            ans=max(ans,now)
        else:
            now=0
    print(ans)
