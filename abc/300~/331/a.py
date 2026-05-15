m,d=map(int,input().split())
y,mo,da=map(int,input().split())

if da<d:
    print(y,mo,da+1)
else:
    if mo==m:
        print(y+1,1,1)
    else:
        print(y,mo+1,1)