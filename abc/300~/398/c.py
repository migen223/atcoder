import sys
n=int(input())
a=list(map(int,input().split()))
ind=[i for i in range(n)]
origin=dict(zip(a,ind))
a.sort()
def mydel(a,big):
    while a[-1]==big:
       a.pop()
       if len(a)==0:
           break

if len(a)==1:
    print(1)
else:
    while a[-1]==a[-2]: 
        big=a[-1]
        mydel(a,big)
        if len(a)==0:
            print(-1)
            sys.exit()
        elif len(a)==1:
            print(origin[a[0]]+1)
            sys.exit()
    print(origin[a[-1]]+1)