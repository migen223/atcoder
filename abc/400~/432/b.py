from itertools import permutations
x=list(input())

ans=10**6
for p in permutations(x):
    if p[0]!="0":
        ans=min(ans,int("".join(p)))
print(ans)

