n=int(input())
grid=[list(input()) for i in range(n)]


out=[]
now=[0,0]
for i in range(n*4-4):
    
    out.append(grid[now[0]][now[1]])
    #print(now[0],now[1])
    if i<n-1:
        now[1]+=1
    elif i<2*(n-1):
        now[0]+=1
    elif i<3*(n-1):
        now[1]-=1
    else:
        now[0]-=1

#print(out)
now=[0,0]
for i in range(n*4-4):
    #print((i-1)%(n*4-4))
    grid[now[0]][now[1]]=int(out[(i-1)%(n*4-4)])
    if i<n-1:
        now[1]+=1
    elif i<2*(n-1):
        now[0]+=1
    elif i<3*(n-1):
        now[1]-=1
    else:
        now[0]-=1
for i in range(n):
    for j in range(n):
        print(grid[i][j],end="")
    print()


"""
00101
11000
00111
00110
00100

00101
11000
00111
00110
10100

"""