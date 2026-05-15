n=int(input())
a,b,c=map(int,input().split())
ans=100000000
for i in range(10000):
    if a*i>n:
        break
    for j in range(10000-i):
        if a*i+b*j>n:
            break
        if (n-a*i-b*j)%c==0:
            n3=(n-a*i-b*j)//c
            if i+j+n3<ans:
                ans=i+j+n3

print(ans)
               
           

