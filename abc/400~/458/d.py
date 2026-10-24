from sortedcontainers import SortedList
x=int(input())
q=int(input())
sl=SortedList([x])

for i in range(q):
    a,b=map(int,input().split())
    sl.add(a)
    sl.add(b)
    #print(sl)
    print(sl[(2*(i+1)+1)//2])
