n=int(input())
h=list(map(int,input().split()))
ma=max(h)

for i in range(n):
    if h[i]==ma:
        print(i+1)