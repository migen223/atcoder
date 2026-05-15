
n,a,b=map(int,input().split())
s=input()
ans=10**18

for i in range(n):
    count=0
    for j in range(n//2):
        #print((j+i)%n,(n-j+i-1)%n)
        #print(s[(j+i)%n],s[(n-j+i-1)%n])
        if s[(j+i)%n]!=s[(n-j+i-1)%n]:
            count+=1
    #print(a*i+count*b," ",count)
    ans=min(ans,a*i+count*b)
print(ans)