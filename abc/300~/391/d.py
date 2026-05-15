from collections import deque
n,w=map(int,input().split())

board={}
for i in range(n):
    x,y=map(int,input().split())
    if x not in board:
        board[x]=[[i+1,y]]
    else:
        board[x].append([i+1,y])
if len(board)==w:
    for v in board:
        board[v]=deque(sorted(board[v],key=lambda x:x[1]))
    #print(board)
    vanish={}
    for i in range(1,n+1):
        vanish[i]=10**12
    for i in range(1,n+1):
        nl=[]
        ma=-1
        f=0
        for j in board:
            if len(board[j])>0:
                num,t=board[j].popleft()
                if ma<t :
                    ma=t
            else:
                ma=10**12
                f+=1
                break
            nl.append(num)
        if f>1:
            break
        for j in nl:
            vanish[j]=ma
    #print(vanish)

    q=int(input())

    for _ in  range(q):
        t,a=map(int,input().split())
        if vanish[a]>t:
            print("Yes")
        else:
            print("No")

else:
    q=int(input())

    for _ in  range(q):
        t,a=map(int,input().split())
        print("Yes")



