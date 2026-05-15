
x,a,d,n=map(int,input().split())


if d>0:
    if x>=(n-1)*d+a:
        print(abs(x-((n-1)*d+a)))
    elif x<=a:
        print(abs(x-a))
    else:
        print(min((x-a)%d,-(x-a)%d))
elif d<0:
    d*=-1
    if x>=a:
        print(abs(x-a))
    elif x<=a-(n-1)*d:
        print(abs(x-(a-(n-1)*d)))
    else:
        #print((x-a)%d,-(x-a)%d)
        print(min((x-a)%d,-(x-a)%d))
else:
    print(abs(x-a))
