
k=int(input())

ans=0
a=1
while a**3<=k:
    b=a
    while a*b**2<=k:
        if k%(a*b)==0 and k//(a*b)>=b:
            #print(a,b,k//(a*b))
            ans+=1
        b+=1
    a+=1

print(ans)

