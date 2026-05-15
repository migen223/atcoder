import sys
n,m,t=map(int,input().split())
a=list(map(int,input().split()))

bonus=[0]*(n+1)
for i in range(m):
    x,y=map(int,input().split())
    bonus[x]=y

#print(bonus)
now=1
for i in range(n-1):
    if t>a[i]:
        t-=a[i]
        now+=1
        t+=bonus[now]
    else:
        print("No")
        sys.exit()
    #print(t)
print("Yes")

    

