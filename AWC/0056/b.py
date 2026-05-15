
n,k=map(int,input().split())
a=list(map(int,input().split()))
a.sort(reverse=True)
for i in range(k):
    a[i]//=2

print(sum(a))