
n,m=map(int,input().split())
i=input()
l=list(map(int,i.split()))

def check(l,n):
    s=0
    for a in range(1,n+1):
        for b in l:
            if a==b:
                s+=1
                break
    if s==n:
        return True
    else:
        return False

c=0
while True:
    if check(l,m):
        del l[len(l)-1]
        c+=1
    else:
        print(c)
        break
