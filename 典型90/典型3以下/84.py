n=int(input())
s=input()
def f(x):
     return x*(x+1)//2
ans=f(n)
count=1
for i in range(n-1):
    if s[i]!=s[i+1]:
        ans-=f(count)
        count=1
    else:
        count+=1
ans-=f(count)
print(ans)
          

