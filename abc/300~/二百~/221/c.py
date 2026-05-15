from itertools import permutations
n=list(input())

ans=0

for p in permutations(n):
    if p[0]!=0:
        for i in range(1,len(n)-1):
            if p[i]!=0:
                ans=max(ans,int("".join(p[:i+1]))*int("".join(p[i+1:])))

if len(n)==2:
    ans=int(n[0])*int(n[1])
print(ans)



