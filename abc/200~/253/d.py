from math import lcm
n,a,b=map(int,input().split())
ans=n*(n+1)//2

ans-=((n//a)*(2*a+(n//a-1)*a))//2
#print(n//a*(2*a+(n//a-1)*a)//2)
#print(n//b*(2*b+(n//b-1)*b)//2)
ans-=((n//b)*(2*b+(n//b-1)*b))//2
#print(ans)
g=lcm(a,b)
ans+=((n//(g))*(2*g+(n//(g)-1)*(g)))//2
print(ans)
