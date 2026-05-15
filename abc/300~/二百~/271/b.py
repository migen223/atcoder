
n,q=map(int,input().split())

ln=[]
for i in range(n):
    l=list(map(int,input().split()))
    ln.append(l[1:])

for i in range(q):
    s,t=map(int,input().split())
    print(ln[s-1][t-1])