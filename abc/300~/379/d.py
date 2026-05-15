
q=int(input())

query=[]
for i in range(q):
    que=list(map(int,input().split()))
    if que[0]==1:
        query.append([1])
    elif que[0]==2:
        t=que[1]
        if len(query)>=1:
            if query[-1][0]==2:
                query[-1][1]+=t
            else:
                query.append(que)
        else:
            query.append(que)
    else:
        query.append(que)


r=[0]
dic={}
count=0
plan=0
now=0
for que in (query):
    #print(que)
    if que[0]==1:
        dic[plan]=count
        plan+=1
    elif que[0]==2:
        count+=1
        r.append(r[-1]+que[1])
    else:
        h=que[1]
        ans=0
        if now in dic:
            while r[-1]-r[dic[now]]>=h:
                ans+=1
                now+=1
                if now not in dic:
                    break
        print(ans)