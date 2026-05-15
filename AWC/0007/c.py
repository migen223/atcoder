from math import ceil
n,k=map(int,input().split())
a=list(map(int,input().split()))

stu=[[a[i],i] for i in range(n)]
def solve(l):
    #print(l)
    if len(l)==1:
        return l
    ne=[[-1,-1] for i in range(ceil(len(l)/2))]
    for i in range(len(l)):
        if ne[i//k][0]<l[i][0]:
            ne[i//k][0]=l[i][0]
            ne[i//k][1]=l[i][1]
    return solve(ne)

print(solve(solve(stu))[0][1]+1)
