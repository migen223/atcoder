from sortedcontainers import SortedList
n=2**20
a=[-1]*n
nota=SortedList([i for i in range(n)])
q=int(input())

for _ in range(q):
    t,x=map(int,input().split())
    if t==1:
        h=x%n
        if a[h]==-1:
            a[h]=x
        else:
            ind=nota.bisect_left(h)
            if ind==len(nota):
                h=nota[0]
            else:
                h=nota[ind]
            a[h]=x
        nota.discard(h)
    elif t==2:
        print(a[x%n])
        #print("ans",a[x%n])

