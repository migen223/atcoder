a,b=map(int,input().split())
s=str(b/a)
if a!=b:
    s+="000000000"
    ans="0."
    for i in range(2,4):
        ans+=s[i]
    if 0<=int(s[5])<=4:
        ans+=s[4]
    else:
        ans+=str(int(s[4])+1)
    print(ans)
else:
    print("1.000")