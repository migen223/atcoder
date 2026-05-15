import sys
n,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

ans=[]
ma=max(a)
for i in range(n):
    if a[i]==ma:
        ans.append(i+1)


for i in range(k):
    if b[i] in ans:
        print("Yes")
        sys.exit()
print("No")