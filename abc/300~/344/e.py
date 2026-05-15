
n=int(input())
a=list(map(int,input().split()))
a.insert(0,-1)
a.append(-1)
q=int(input())
dic={}
for i in range(1,n+1):
    dic[a[i]]=[a[i-1],a[i+1]]
root=a[1]

for  _ in range(q):
    que=list(map(int,input().split()))
    if que[0]==1:
        x,y=que[1],que[2]
        aft=dic[x][1]
        dic[x][1]=y
        dic[y]=[x,aft]
        if aft!=-1:
            dic[aft][0]=y
    elif que[0]==2:
        x=que[1]
        pre,aft=dic[x]
        dic.pop(x)
        if pre==-1 :
            dic[aft][0]=-1
            root=aft
        elif aft==-1:
            dic[pre][1]=-1
        else:
            dic[pre][1]=aft
            dic[aft][0]=pre
    """
    ans=[]
    now=root
    while True:
        ans.append(now)
        if dic[now][1]!=-1:
            now=dic[now][1]
        else:
            break
    print("ans",*ans)
    print(dic)"""

ans=[]
now=root
while True:
    ans.append(now)
    if dic[now][1]!=-1:
        now=dic[now][1]
    else:
        break
print(*ans)