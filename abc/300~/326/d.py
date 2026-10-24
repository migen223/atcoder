import sys
from itertools import permutations
n=int(input())
r=input()
c=input()
s=["A","B","C"]
dic={"A":0,"B":1,"C":2}

def check(board):
    row=[]
    col=[]
    for i in range(n):
        for j in range(n):
            if board[i][j]!=".":
                row.append(board[i][j])
                break
    for i in range(n):
        for j in range(n):
            if board[j][i]!=".":
                col.append(board[j][i])
                break
    row="".join(row)
    col="".join(col)
    #print(row,col,r,c)
    if row==r and col==c:
        return True
    return False
                
for p1 in permutations(range(n)):
    for p2 in permutations(range(n)):
        for p3 in permutations(range(n)):
            f=0
            p=[p1,p2,p3]
            #print(*p)
            for i in range(n):
                if len(set([p1[i],p2[i],p3[i]]))!=3:
                    f+=1
                    break
            if f>0:
                continue
            board=[["." for _ in range(n)] for _ in range(n)]
            for i in range(3):
                for j in range(n):
                    board[j][p[i][j]]=s[i]
            #for i in range(n):
             #   print(*board[i])
            #print()  
            if check(board):
                print("Yes")
                for i in range(n):
                    print("".join(board[i]))
                sys.exit()
            
print("No")

