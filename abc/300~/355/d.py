from bisect import bisect_right,bisect_left
n=int(input())

sect=[]
ls=[]
rs=[]
for i in range(n):
    l,r=map(int,input().split())
    sect.append((l,r))
    ls.append(l)
    rs.append(r)

ls.sort()
rs.sort()

ans=(n*(n-1))//2
for i in range(n):
    ind=bisect_right(rs,ls[i]-1)
    ans-=ind
print(ans)




