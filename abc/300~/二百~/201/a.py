from itertools import permutations
import sys
a,b,c=map(int,input().split())

for p in permutations([a,b,c]):
    if p[2]-p[1]==p[1]-p[0]:
        print("Yes")
        sys.exit()
print("No")
