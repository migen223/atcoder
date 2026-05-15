x=input()
ans=""

k=0
for i in range(len(x)):
    if x[i]==".":
        k=int(x[i+1])
        break
    ans+=x[i]
ans=int(ans)

if k>=5:
    ans+=1
print(ans)
