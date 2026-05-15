
sx,sy=map(int,input().split())
tx,ty=map(int,input().split())


def check(n):
    return n%2==0

if tx>sx:
    if check(ty):
        if check(tx):
            tx+=1
    else:
        if not check(tx):
            tx+=1
    if check(sy):
        if not check(sx):
            sx-=1
    else:
        if check(sx):
            sx-=1
    movexy=tx-sx-1
    if movexy<abs(sy-ty):
        print(abs(sy-ty))
    elif movexy>abs(sy-ty):
        x=sx+1+abs(sy-ty)
        tx-=1
        print((tx-sx)//2)
    else:
        print(movexy)
elif tx<sx:
    if check(sy):
        if not check(sx):
            sx+=1
    else:
        if check(sx):
            sx+=1
    
    if check(ty):
        if check(tx):
            tx-=1
    else:
        if not check(tx):
            tx-=1
    
    movexy=sx-tx-1
    if movexy<abs(sy-ty):
        print(abs(sy-ty))
    elif movexy>abs(sy-ty):
        x=sx-1+abs(sy-ty)
        tx+=1
        print((tx-sx)//2)
    else:
        print(movexy)
else:
    print(abs(sy-ty))



        