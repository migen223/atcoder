q=int(input())
snake=[]
top=0
minus=0
for i in range(q):
    que=input().split()
    #print(que)
    #print(snake)
    if que[0]=="1":
        l=int(que[1])
        if len(snake)==0:          
            #print(l)
            snake.append([0,l])
        else:
            #print(snake[-1][1],l)
            #print(l)
            snake.append([snake[-1][1],snake[-1][1]+l])
    elif que[0]=="2":
        minus=snake[top][1]
        top+=1
        
    else:
        k=int(que[1])-1
        print(snake[top+k][0]-minus)
    