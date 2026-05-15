from itertools import permutations
s=input().split()
k=int(s[1])
se=set()
for p in permutations(s[0]):
    se.add(tuple(p))
l=list(se)
l.sort()
print("".join(l[k-1]))