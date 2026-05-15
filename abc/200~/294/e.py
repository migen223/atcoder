from collections import deque
l,n,m=map(int,input().split())

up=[]
bot=deque([])

now=0
for i in range(n):
    v,l=map(int,input().split())
    up.append((v,now+1,now+l))
    now+=l

now=0
for  i in range(m):
    v,l=map(int,input().split())
    bot.append([v,now+1,now+l])
    now+=l

ans=0
for i in range(n):
    while up[i][2]>bot[0][2]:
        if up[i][0]==bot[0][0]:
            ans+=bot[0][2]-bot[0][1]+1
        bot.popleft()
    if up[i][0]==bot[0][0]:
        ans+=up[i][2]-bot[0][1]+1
    if up[i][2]==bot[0][2]:
        bot.popleft()
    else:
        bot[0][1]=up[i][2]+1
    #print(bot)
print(ans)
