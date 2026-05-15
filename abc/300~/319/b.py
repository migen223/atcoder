
n=int(input())


ans=[]
for i in range(n+1):
    now="-"
    for j in range(1,10):
        if n%j==0:
            if i%(n//j)==0:
                now=str(j)
                break
    ans.append(now)
print("".join(ans))