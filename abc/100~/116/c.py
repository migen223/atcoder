n=int(input())
h=list(map(int,input().split()))
ansl=[0]*n
mini=1000
ind=-1
for i in range(n):
    if mini>h[i]:
        mini=h[i]
        ind=i
miniind=ind
maxind=ind
ansl[ind]=h[ind]
while (miniind>0):
    if h[miniind]<h[miniind-1]:
        ansl[miniind-1]=h[miniind-1]-h[miniind]
    miniind-=1
while (maxind<n-1):
    if h[maxind]<h[maxind+1]:
        ansl[maxind+1]=h[maxind+1]-h[maxind]
    maxind+=1
print(sum(ansl))

