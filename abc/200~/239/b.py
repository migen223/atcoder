
x=list(input())

ans=""
if x[0]=="-":
    if len(x)>=3:
        if x[-1]=="0":
            x.pop()
            print("".join(x))
        else:
            x.pop()
            n=int("".join(x))
            n-=1
            print(n)
    else:
        print(-1)
else:
    if len(x)>=2:
        x.pop()
        print("".join(x))
    else:
        print(0)

