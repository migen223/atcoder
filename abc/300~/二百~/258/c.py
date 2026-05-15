
n,q=map(int,input().split())
s=list(input())

offset=0
for i in range(q):
    t,x=map(int,input().split())
    if t==1:
        offset+=x
    else:
        print(s[(x-1-offset)%n])

