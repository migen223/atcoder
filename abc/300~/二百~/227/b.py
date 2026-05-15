

n=int(input())
s=list(map(int,input().split()))

ans=n
for i in range(n):
    f=0
    for a in range(1,251):
        for b in range(1,251):
            if s[i]==4*a*b+3*a+3*b:
                f+=1
                ans-=1
                break
        if f>=1:
            break

print(ans)


