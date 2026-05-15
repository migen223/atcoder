
n=int(input())
h=list(map(int,input().split()))

now=[h[-1]]
ans=[0]*n
for i in range(1,n):
    ans[-1-i]=len(now)
    while h[-1-i]>now[-1]:
        now.pop()
        if len(now)==0:
            break
    now.append(h[-1-i])
    #print(now)
   
print(*ans)
