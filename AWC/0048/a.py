
n=int(input())

ans=[]
for i in range(n):
    s,k=input().split()
    k=int(k)
    if k%2==0:
        ans.append(s)
    else:
        if s=="Yes":
            ans.append("No")
        else:
            ans.append("Yes")

for i in range(n):
    print(ans[i])
