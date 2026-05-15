n=int(input())
p=list(map(int,input().split()))#見てる人
q=list(map(int,input().split()))#持つ数
ans=[]
dic=dict(zip(q,p))
for i in range(1,n+1):
    ans.append(q[dic[i]-1])
print(*ans)
