import copy
n,d=map(int,input().split())
snake=[]
for i in range(n):
    snake.append(list(map(int,input().split())))

for i in range(d):
    ans=0
    for j in range(n):
        snake[j][1]+=1
        ans=max(ans,snake[j][0]*snake[j][1])
    print(ans)
"""
if n>=d:
    for i in range(d):
        for j in range(i+1):
            #print(i,j)
            snake[j][1]=snakeo[j][1]+i+1
        ans=0
        for k in snake:
            ans=max(ans,k[0]*k[1])
        #print(snakeo)
        print(snake)
        print(ans)
else:
    for i in range(d):
        for j in range(min(i+1,n)):
            #print(i,j)
            snake[j][1]=snakeo[j][1]+i+1
        ans=0
        for k in snake:
            ans=max(ans,k[0]*k[1])
        #print(snakeo)
        print(snake)
        print(ans)
"""