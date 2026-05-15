s=list(input())
#print(s)
ans=0
t=""
ren0=0
for i in range(len(s)):
    #print(t)
    if s[i]!="0":
        #print("0じゃないよ")
        t+=s[i]
        ans+=1
        ren0=0
    else:
        #print("０だよ")
        t+="0"
        ans+=1
        if ren0==1:
            ans-=1
            ren0=0
        else:
            ren0+=1
print(ans)