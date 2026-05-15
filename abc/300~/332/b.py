k,g,m=map(int,input().split())
gl=0
mg=0
for i in range(k):
    if gl==g:
        gl=0
    elif mg==0:
        mg=m
    else:
        while (mg!=0 and gl!=g):
            mg-=1
            gl+=1
print(gl,mg)