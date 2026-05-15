
n,q=map(int,input().split())
pc=[[] for _ in range(n+1)]

query=[]
for _ in range(q):
    que=input().split()
    query.append(que)

ans=[]
now="0"
for i in range(q-1,-1,-1):
    que=query[i]
    if que[0]=="1":
        p=que[1]
        if now==p:
            now="0"
    elif que[0]=="2":
        p,s=que[1],que[2]
       # print("now,p",now,p)
        if now==p:
            ans.append(s) 
    elif que[0]=="3":
        p=que[1]
        if now=="0":
            now=p
    #print("now",now,que,ans)
    
ans.reverse()

for i in range(len(ans)):
    print(ans[i],end="")
print()
