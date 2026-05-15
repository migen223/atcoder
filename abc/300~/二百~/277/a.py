n,x=map(int,input().split())
s=list(map(int,input().split()))
for i in range(n):
    if s[i]==x:
        print(i+1)
        break