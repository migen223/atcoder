
n=int(input())
a=list(map(int,input().split()))
balls=[]
for i in range(n):
    balls.append(a[i])
    while True:
        if len(balls)<=1:
            break
        elif balls[-1]!=balls[-2]:
            break
        else:
            ball=balls.pop()
            ball=balls.pop()
            balls.append(ball+1)
    #print(balls)
print(len(balls))