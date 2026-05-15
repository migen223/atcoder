import sys
n=int(input())
grida=[list(map(int,input().split())) for i in range(n)]
gridb=[list(map(int,input().split())) for i in range(n)]

def right_rot90(S):
    return list(zip(*S[::-1]))

a1=0
for i in range(n):
    for j in range(n):
        if grida[i][j]==1:
            a1+=1

for i in range(4):
    f=0
    grida=right_rot90(grida)
    for j in range(n):
        for k in range(n):
            if grida[j][k]==1 and gridb[j][k]==1:
                f+=1
    if f==a1:
        print("Yes")
        sys.exit()
print("No")
