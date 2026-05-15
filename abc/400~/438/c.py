
n=int(input())
a=list(map(int,input().split()))

stack=[[a[0],1]]
for i in range(1,n):
    if len(stack)>0:
        if a[i]==stack[-1][0]:
            stack[-1][1]+=1
            if stack[-1][1]==4:
                stack.pop()
        else:
            stack.append([a[i],1])
    else:
        stack.append([a[i],1])
    
ans=0
for i in range(len(stack)):
    ans+=stack[i][1]
print(ans)
