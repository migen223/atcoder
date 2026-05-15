
n,q=map(int,input().split())

dic={}#数字から番号
balls=[i for i in range(n+1)]
for i in range(1,n+1):
    dic[i]=i



for i in range(q):
    x=int(input())
    ind=dic[x]
    if ind==n:
        ind2=ind-1
    else:
        ind2=ind+1
    dic[balls[ind]],dic[balls[ind2]]=dic[balls[ind2]],dic[balls[ind]]
    balls[ind],balls[ind2]=balls[ind2],balls[ind]
    

for i in range(1,n+1):
    print(balls[i],end=" ")