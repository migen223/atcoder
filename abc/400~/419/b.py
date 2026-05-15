q=int(input())
box=[]
for _ in range(q):
    que=input()
    if len(que)>=3:
        number,x=map(int,que.split())
        box.append(x)
        box.sort()
    else:
        print(box.pop(0))