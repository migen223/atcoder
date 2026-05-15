from itertools import combinations
grid=[list(input()) for _ in range(9)]
bone=[]
for i in range(9):
    for j in range(9):
        if grid[i][j]=="#":
            bone.append((i,j))
ans=0
for c in combinations(bone,4):
    #print(c)
    l1=(c[0][0]-c[1][0])**2+(c[0][1]-c[1][1])**2
    l2=(c[0][0]-c[2][0])**2+(c[0][1]-c[2][1])**2
    l3=(c[0][0]-c[3][0])**2+(c[0][1]-c[3][1])**2
    l4=(c[2][0]-c[1][0])**2+(c[2][1]-c[1][1])**2
    l5=(c[3][0]-c[1][0])**2+(c[3][1]-c[1][1])**2
    l6=(c[2][0]-c[3][0])**2+(c[2][1]-c[3][1])**2

    l=[l1,l2,l3,l4,l5,l6]
    l.sort()
    #print(l)
    if l[0]==l[1]==l[2]==l[3] and l[4]==l[5] and l[0]<l[5]:
        if l[0]+l[1]==l[5]:
            ans+=1
print(ans)


