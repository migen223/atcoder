d=input()
def dim(s):
    if s=="N":
        return "S"
    elif s=="S":
        return "N"
    elif s=="E":
        return "W"
    else:
        return "E"
ans=""
for i in range(len(d)):
    ans+=dim(d[i])
print(ans)