
h,w=map(int,input().split())
n=min(h,w)
ans=[0]*(n)
grid=[list(input()) for i in range(h)]

visit=set()
for i in range(h):
    for j in range(w):
        count=0
        now=[i,j]
        if grid[i][j]=="#" and (i,j) not in visit:
            while grid[now[0]][now[1]]=="#" and 0<=now[0]<=h-1 and 0<=now[1]<=w-1:
                visit.add((now[0],now[1]))
                now[0]+=1
                now[1]+=1
                count+=1
                if not (0<=now[0]<=h-1 and 0<=now[1]<=w-1):
                    break
            other=[i,j+count-1]
            for k in range(count):
                visit.add((other[0],other[1]))
                other[0]+=1
                other[1]-=1
            ans[count//2-1]+=1
print(*ans)
#print(visit)

        

