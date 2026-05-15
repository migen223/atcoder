n=int(input())

def change(n):
    res=0
    for i in range(len(str(n))):
        res+=int(str(n)[i])**2
    return res

ans=n
for i in range(10**6):
    ans=change(ans)

if ans==1:
    print("Yes")
else:
    print("No")