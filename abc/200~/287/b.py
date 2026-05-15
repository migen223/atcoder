n,m=map(int,input().split())
s=[]
t=[]
for i in range(n):
    s.append(list(input()))
for i in range(m):
    t.append(list(input()))



ans=0
for i in range(n):
    last=[s[i][-3],s[i][-2],s[i][-1]]
    #print(last)
    if last in t:
        ans+=1
print(ans)

