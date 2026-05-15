from itertools import product
n,m=map(int,input().split())
#2^16=65536<10^5
jouken=[]
for i in range(m):
    ab=set(map(int,input().split()))
    jouken.append(ab)
k=int(input())
max=-1
ball=[]
for _ in range(k):
    cd=list(map(int,input.split()))
    ball.append(cd)



