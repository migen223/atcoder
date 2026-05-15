from itertools import product
n=int(input())
for i in product([i for i in range(n+1)],repeat=3):
    l=list(i)
    if l[0]+l[1]+l[2]<=n:
        print(l[0],l[1],l[2])