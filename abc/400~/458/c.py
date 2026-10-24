
s=input()
n=len(s)

cs=[]
for i in range(n):
    if s[i]=="C":
        cs.append(i)

ans=len(cs)
for i in range(len(cs)):
    c=cs[i]
    ans+=min(n-1-c,c)

print(ans)