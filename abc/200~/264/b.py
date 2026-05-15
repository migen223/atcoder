
r,c=map(int,input().split())

r-=1
c-=1
def check(r,c):
    if r==0 or r==14 or c==0 or c==14:
        return "black"
    elif (r==2 and c!=1 and c!=13) or (r==12 and c!=1 and c!=13) or (c==2 and r!=1 and r!=13) or (c==12 and r!=1 and r!=13) :
        return "black"
    elif (r==4 and c!=1 and c!=13 and c!=3 and c!=11) or (r==10 and c!=1 and c!=13 and c!=3 and c!=11) or (c==4 and r!=1 and r!=13 and r!=3 and r!=11) or (c==10 and r!=1 and r!=13 and r!=3 and r!=11) :
        return "black"
    elif (r==6 and c!=1 and c!=13 and c!=3 and c!=11 and c!=5 and c!=9) or (r==8 and c!=1 and c!=13 and c!=3 and c!=11 and c!=5 and c!=9) or (c==6 and r!=1 and r!=13 and r!=3 and r!=11 and r!=5 and r!=9) or (c==8 and r!=1 and r!=13 and r!=3 and r!=11 and r!=5 and r!=9) :
        return "black"
    else:
        return "white"

grid=[[] for i in range(15)]
for i in range(15):
    for j in range(15):
        if check(i,j)=="black":
            grid[i].append("#")
        else:
            grid[i].append(".")
print(check(r,c))
