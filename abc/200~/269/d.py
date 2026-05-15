
n=int(input())
se=set()
for i in range(n):
    x,y=map(int,input().split())
    se.add((x,y))


dy=[-1,-1,0,0,1,1]
dx=[-1,0,-1,1,0,1]
visit=set()
count=0
for i in se:
    if i not in visit:
        count+=1
        visitable=[i]
        while visitable:
            now=visitable.pop()
            visit.add(now)
            for j in range(6):
                if (now[0]+dy[j],now[1]+dx[j]) in se and (now[0]+dy[j],now[1]+dx[j]) not in visit:
                    visitable.append((now[0]+dy[j],now[1]+dx[j]))

print(count)