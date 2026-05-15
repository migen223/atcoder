from collections import deque
n=int(input())
s=deque(input())

ans=[]
while s:
    if s[0]=="o":
        s.popleft()
        if len(s)==0:
            break
    else:
        break

for i in range(len(s)):
    ans.append(s[i])

print("".join(ans))