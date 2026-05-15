n=int(input())
w=input()
an=list(map(int,w.split()))
w=input()
bn=list(map(int,w.split()))
an.sort()
bn.sort()
e=0
for i in range(n):
    e+=abs(an[i]-bn[i])
print(e)
