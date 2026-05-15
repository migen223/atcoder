
n=int(input())
a=list(map(int,input().split()))

balls=[]

ans=0
for i in range(n):
    if len(balls)==0:
        balls.append([a[i],1])
        ans+=1
    else:
        if balls[-1][0]==a[i] and balls[-1][1]>=balls[-1][0]-1:
            balls[-1][1]+=1
            ans+=1
            #print(balls)
            while balls[-1][1]-balls[-1][0]>=0:
                balls[-1][1]-=balls[-1][0]
                ans-=balls[-1][0]
            if balls[-1][1]==0:
                balls.pop()
        elif balls[-1][0]==a[i]:
            balls[-1][1]+=1
            ans+=1
        else:
            balls.append([a[i],1])
            ans+=1
    #print(balls)
    print(ans)





