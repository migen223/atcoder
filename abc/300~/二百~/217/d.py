from sortedcontainers import SortedList
l,q=map(int,input().split())

wood=SortedList([0,l])

for i in range(q):
    c,x=map(int,input().split())
    #print(wood)
    if c==1 :
        wood.add(x)
    elif c==2:
        ind=wood.bisect_left(x)
        print(wood[ind]-wood[ind-1])