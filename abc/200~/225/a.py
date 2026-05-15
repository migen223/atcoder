from itertools import permutations
s=input()
se=set()

for p in permutations(s):
    se.add(p)

print(len(se))
