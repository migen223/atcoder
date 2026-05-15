n=int(input())
p=list(map(int,input().split()))
p.reverse()
p1=p.pop()
if n==1:
    print(0)
else:

    if max(p)<p1:
        print(0)
    else:
        print(max(p)-p1+1)