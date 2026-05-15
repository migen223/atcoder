from sortedcontainers import SortedList
n,q=map(int,input().split())
a=list(map(int,input().split()))
asort=SortedList(a)
dic={}
for i in range(n):
    dic[i+1]=a[i]
for _ in range(q):
    k=int(input())
    b=list(map(int,input().split()))
    d=[]
    for dis in b:
        d.append(dic[dis])
        asort.discard(dic[dis])
    print(asort[0])
    for app in d:
        asort.add(app)