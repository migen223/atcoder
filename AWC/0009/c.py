
n,t,k=map(int,input().split())
h=list(map(int,input().split()))
h.sort()

while h[-1]-(t+k)>=h[0]:
    h.pop()

print(len(h))