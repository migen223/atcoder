from collections import  Counter
n=int(input())
a=list(map(int,input().split()))

ans=0

c=Counter(a)


for i in c.most_common():
    if i[1]>=2:
        ans+=((i[1]*(i[1]-1))//2)*(n-i[1])
    else:
        break

print(ans)
        

