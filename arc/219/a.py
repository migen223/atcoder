
n,m=map(int,input().split())

def cahnge(s):
    res=[]
    for i in s:
        if i=="0":
            res.append("1")
        else:
            res.append("0")
    return "".join(res)


ban=set()
for _ in range(n):
    s=input()
    ban.add(cahnge(s))


if len(ban)==2**m:
    print("No")
else:
    print("Yes")
    for i in range(len(ban)+2):
        b=bin(i)[2:]
        bl=[]
        if len(b)<=m:
            for j in range(m-len(b)):
                bl.append("0")
        bl.append(b)
        #print(b,i,bl)
        b="".join(bl)
        if b not in ban:
            print(b)
            break