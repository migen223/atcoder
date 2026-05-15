cube1=list(map(int,input().split()))
cube2=list(map(int,input().split()))
def co(l0,r0,l1,r1):
    if r0<=l1:
        return False
    elif r1<=l0:
        return False
    else:
        return True
if co(cube1[0],cube1[3],cube2[0],cube2[3]) and co(cube1[1],cube1[4],cube2[1],cube2[4]) and co(cube1[2],cube1[5],cube2[2],cube2[5]):
    print("Yes")
else:
    print("No")