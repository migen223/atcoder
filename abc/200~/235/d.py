from collections import deque
import sys
a,n=map(int,input().split())


#"""
def swap(n):
    ans=[]
    s=str(n)
    for i in range(1,len(s)):
        ans.append(s[i])
    ans.append(s[0])
    return int("".join(ans))

numbers=[-1]*(10**6)
numbers[n]=0
numbers[1]=10**32

visitable=[[n,0]]

while visitable:
    now=visitable.pop()
    #print(now,numbers[now[0]])
    if now[0]%a==0:
        if numbers[now[0]//a]==-1:
            numbers[now[0]//a]=now[1]+1
            visitable.append([now[0]//a,now[1]+1])
        else:
            if numbers[now[0]//a]>now[1]+1:
                numbers[now[0]//a]=now[1]+1
                visitable.append([now[0]//a,now[1]+1])
    if now[0]>=11 and str(now[0])[1]!="0":
        s=str(now[0])
        num=now[0]
        #print(f"s={s}")
        num=swap(num)
        #print(num)
        if numbers[num]==-1:
            numbers[num]=now[1]+1
            visitable.append([num,now[1]+1])
        else:
            if numbers[num]>now[1]+1:
                numbers[num]=now[1]+1
                visitable.append([num,now[1]+1])
    
if numbers[1]==10**32:
    print(-1)
else:
    print(numbers[1])
#"""


"""ACコード
def swap(n):
    ans=[]
    s=str(n)
    ans.append(s[-1])
    for i in range(len(s)-1):
        ans.append(s[i])
    return int("".join(ans))

visitable=deque([[1,0,False]])
numbers=[-1]*(10**6)

while visitable:
    now=visitable.popleft()
    if now[0]==n:
        print(now[1])
        sys.exit()
    if now[0]*a<10**6: 
        if numbers[now[0]*a]==-1:
            numbers[now[0]*a]=now[1]+1
            visitable.append([now[0]*a,now[1]+1])
    if now[0]%10!=0 and now[0]>=11:
        s=str(now[0])
        num=now[0]
        #print(f"s={s}")

        num=swap(num)
        #print(num)
        if numbers[num]==-1:
            numbers[num]=now[1]+1
            visitable.append([num,now[1]+1])
            
print(-1)
"""


