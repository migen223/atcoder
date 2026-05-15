
n,x=map(int,input().split())
a=list(map(int,input().split()))

anss=set([x])
now=a[x-1]

while now not in anss:
    anss.add(now)
    now=a[now-1]
print(len(anss))
