x=list(input())
ans=""
for i in range(3):
    if x[-1]=="0":
        x.pop()
    else:
        break
if x[-1]==".":
    x.pop()
print("".join(x))
