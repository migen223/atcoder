x,c=map(int,input().split())
ans=0

while x>=0:
    x-=(1000+c)
    ans+=1
print((ans-1)*1000)