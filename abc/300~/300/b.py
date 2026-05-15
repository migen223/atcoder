import sys
from copy import deepcopy
h,w=map(int,input().split())

grida=[list(input()) for i in range(h)]
gridb=[list(input()) for i in range(h)]



for s in range(h):
    for t in range(w):
        count=0
        new_grid=deepcopy(grida)

        for i in range(w):
            l=[]
            for j in range(h):
                #print((j+2)%h,i)
                l.append(grida[(j+s)%h][i])
            for j in range(h):
                new_grid[j][i]=l[j]
            #print(f"S={s} t={t} ")
            #print(l)

        for i in range(h):
            l=[]
            for j in range(w):
                #print((j-1)%h,i)
                l.append(new_grid[i][(j+t)%w])
            for j in range(w):
                new_grid[i][j]=l[j]
            #print(f"S={s} t={t}")
            #print(l)
        check=0
        for i in range(h):
            f=0
            for j in range(w):
                if gridb[i][j]!=new_grid[i][j]:
                    f+=1
                    check+=1
                    break
            if f!=0:
                break
       # print()
        if check==0:
            """
            for i in range(h):
                print(*new_grid[i])
            print("ng")
            for i in range(h):
                print(*gridb[i])
            print("b")
            """
            print("Yes")
            sys.exit()

        #print(s,t)
        #for i in range(h):
         #   print(*new_grid[i])

print("No")


"""
new_grid=grida.copy()
for i in range(w):
    l=[]
    for j in range(h):
        #print((j-1)%h,i)
        l.append(grida[(j+2)%h][i])
    for j in range(h):
        new_grid[j][i]=l[j]

for i in range(h):
    print(*new_grid[i])
for i in range(h):
    l=[]
    for j in range(w):
        #print((j-1)%h,i)
        l.append(grida[i][(j+1)%w])
    for j in range(w):
        new_grid[i][j]=l[j]

"""


