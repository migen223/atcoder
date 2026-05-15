n,q=map(int,input().split())
i=input()
an=list(map(int,i.split()))
count=0
for _ in range(q):
    t,x,y=map(int,input().split())
    if t==1:
        an[(x-1-count)%n],an[(y-1-count)%n]=an[(y-1-count)%n],an[(x-1-count)%n]
    if t==2:
        count+=1
    if t==3:
        print(an[(x-1-count)%n])
