n=int(input())
two=bin(n)
ans=0
for i in range(len(two)):
    if two[-1-i]=="0":
        ans+=1
    else:
        break
print(ans)
