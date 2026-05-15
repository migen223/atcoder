import sys
n,k,x=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
alc=0

for i in range(n-k):
    a.pop()
ans=n-k
for i in range(k):
    alc+=a[-i-1]
    ans+=1
    if alc>=x:
        print(ans)
        sys.exit()

print(-1)


"""
alcl=[a[i] for i in range(n)]
for i in range(n-k):
    alcl[-i-1]=0
alcl.sort()
print(alcl)
for i in range(n):
    alc+=alcl[i]
    if alc>=x:
        print(i+1)
        sys.exit()

print(-1)
"""
