from collections import deque
n,m=map(int,input().split())
a=list(map(int,input().split()))
stack=[]
ans=[]
re=[]
for i in range(m):
    if len(stack)==0:
        stack.append(a[i])
    else:
        if a[i]-stack[-1]==1:
            stack.append(a[i])
        else:
            #print(stack)
            re.append([stack[0],stack[-1]])
            stack=[a[i]]
#print(stack)
if len(stack)>0:
    re.append([stack[0],stack[-1]])

if m>0:
    re=deque(re)
    next=1
    while re:
        now=re.popleft()
        if next<now[0]:
            for i in range(next,now[0]):
                ans.append(i)
        for i in range(now[1]+1,now[0]-1,-1):
            ans.append(i)
        next=now[1]+2
    for i in range(next,n+1):
        ans.append(i)
    print(*ans)
else:
    print(*[i for i in range(1,n+1)])
    
