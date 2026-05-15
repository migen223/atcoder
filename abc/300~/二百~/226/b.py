
n=int(input())

se=set()
for i in range(n):
    l=list(map(int,input().split()))
    se.add(tuple(l[1:]))

print(len(se))