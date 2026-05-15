
a,b,c,d=map(int,input().split())

if b>=d*c:
    print(-1)


else:
    if a%(d*c-b)==0:
        print(a//(d*c-b))
    else:
        print(a//(d*c-b)+1)