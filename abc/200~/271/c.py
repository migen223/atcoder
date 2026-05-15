from collections import deque
n=int(input())
a=list(map(int,input().split()))
a.sort()
nokori=0
se=set()
for i in range(n):
    if a[i]<=n:
        if a[i] not in se:
            se.add(a[i])
        else:
            nokori+=1
    if a[i]>n:
        nokori+=1

if len(se)>=1:
    book=list(se)
    book.sort()
    bd=deque(book)
    now=0
    while bd :
        if now+1==bd[0]:
            now=bd.popleft()
        else:
            if nokori>=2:
                nokori-=2
                now+=1
            elif nokori==1:
                nokori-=1
                now+=1
                bd.pop()
            else:
                if len(bd)>=2:
                    bd.pop()
                    bd.pop()
                    now+=1
                else:
                    break
        #print(nokori)
        #print(now)
        #print(bd)
    
    while nokori>=2:
        nokori-=2
        now+=1
    print(now)
elif len(se)==0:
    print(0)



