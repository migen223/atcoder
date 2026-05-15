import sys
n=int(input())

s=[list(input()) for i in range(n)]
t=[list(input()) for i in range(n)]

def right_rot90(S):
    return list(zip(*S[::-1]))
def printout(s):
    for i in range(len(s)):
        print(*s[i])

s1=right_rot90(s)
s2=right_rot90(s1)
s3=right_rot90(s2)

gs=set()
for i in range(n):
    for j in range(n):
        if t[i][j]=="#":
            if len(gs)==0:
                start1=(i,j)
            gs.add((i,j))


shapes=[s,s1,s2,s3]
for sh in shapes:
    d=[]
    block=[]
    for i in range(n):
        for j in range(n):
            if sh[i][j]=="#":
                if len(d)==0:
                    d.append(start1[0]-i)
                    d.append(start1[1]-j)
                block.append([i,j])
                #print(start1[0],start1[1],i,j)

    #printout(sh)
    #print(d)
    #print(gs)
    #print(start1)
    count=0
    for b in block:
        ny=b[0]+d[0]
        nx=b[1]+d[1]
        if 0<=ny<=n-1 and 0<=nx<=n-1:
            if (ny,nx) in gs:
                count+=1
    if count==len(gs) and len(block)==len(gs):
        print("Yes")
        sys.exit()

print("No")

