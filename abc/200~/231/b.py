from collections import Counter
n=int(input())
s=[input() for i in range(n)]
c=Counter(s)
print(c.most_common()[0][0])