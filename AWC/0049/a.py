
n,l,p,q=map(int,input().split())

for i in range(n):
    s=int(input())
    if s<=l:
        print((s*p)//100)
    else:
        print((l*p+(s-l)*q)//100)
        