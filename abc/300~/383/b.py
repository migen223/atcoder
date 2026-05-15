h,w,d=map(int,input().split())
office=[]
for i in range(h):
    office.append(list(input()))
floar=[]
for i in range(h):
    for j in range(w):
        if office[i][j]==".":
            floar.append([i,j])
ans=0
for k in range(len(floar)-1):
    for l in range(k+1,len(floar)):
        count=0
        change=[]
        for onetwo in [floar[k],floar[l]]:
            for i in range(h):
                for j in range(w):
                    if abs(onetwo[0]-i)+abs(onetwo[1]-j)<=d and office[i][j]==".":
                        count+=1
                        office[i][j]="#"
                        change.append([i,j])
        for i in range(len(change)):
            office[change[i][0]][change[i][1]]="."
        ans=max(ans,count)
print(ans)
