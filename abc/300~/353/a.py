n=int(input())
h=list(map(int,input().split()))
for i in range(n):
    if h[0]<h[i]:
        print(i+1)
        break
    if i==n-1:
        print(-1)