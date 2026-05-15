from collections import deque
q=int(input())

now=1
st=deque([1])
p=998244353


for _ in range(q):
    que=list(map(int,input().split()))
    if que[0]==1:
        x=que[1]
        now*=10
        now+=x
        now%=p
        st.append(x)
    elif que[0]==2:
        top=st.popleft()
        now-=top*(pow(10,len(st),p))
        now%=p
    else:
        print(now%p)


