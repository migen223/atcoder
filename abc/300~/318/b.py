n=int(input())

se=set()
for i in range(n):
    a,b,c,d=map(int,input().split())
    for j in range(a,b):
        for k in range(c,d):
            se.add((j,k))
print(len(se))
