
n=int(input())

def f(x):
    x=str(x)
    ans=0
    for i in x:
        ans+=int(i)
    return ans

ans=[1,1]
for i in range(n-1):
    ans.append(ans[-1]+f(ans[-1]))
    #print(f(ans[-1]))
    #print(ans)
print(ans[-1])

