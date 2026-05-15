n,k=map(int,input().split())
name=[]
for i in range(n):
    name.append(input())
ans=[]
for i in range(k):
    ans.append(name[i])
ans.sort()
for i in range(k):
    print(ans[i])