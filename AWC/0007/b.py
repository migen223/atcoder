

n,k=map(int,input().split())

room=[]
for i in range(n):
    m=int(input())
    w=set(input().split())
    room.append(w)

ans=0
for i in range(n-1):
    for j in range(i+1,n):
        if len(room[i]&room[j])>=k:
            ans+=1
print(ans)
