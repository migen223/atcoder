n,q=map(int,input().split())
doragon=[[i+1,0] for i in range(n)]
doragon.reverse()
head=[1,0]
offset=0
for i in range(q):
    que=input().split()
    if que[0]=="1":
        if que[1]=="U":
            head[1]+=1
        elif que[1]=="D":
            head[1]-=1
        elif que[1]=="R":
            head[0]+=1
        else:
            head[0]-=1
        #print(que[1],head)
        doragon.append([head[0],head[1]])
        offset+=1
    else:
        p=int(que[1])
        print(*doragon[n-p+offset])
#print(doragon)
