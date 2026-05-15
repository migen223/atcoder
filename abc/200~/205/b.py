from collections import Counter
n=int(input())
a=list(map(int,input().split()))
if len(Counter(a))==n:
    print("Yes")
else:
    print("No")