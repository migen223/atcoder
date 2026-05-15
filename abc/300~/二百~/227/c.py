
n=int(input())
ans=0

a=1
while a**3<=n:
    b=a
    while a*b*b<=n:
        if b>n//(a*b):
            break
        else:
            ans+=n//(a*b)-b+1
        b+=1
    a+=1
print(ans)

