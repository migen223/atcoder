

n,a,b=map(int,input().split())

for i in range(n*a):
    for j in range(n*b):
        if (i//a)%2==0:
            if (j//b)%2==0:
                print(".",end="")
            else:
                print("#",end="")
        else:
            if (j//b)%2==0:
                print("#",end="")
            else:
                print(".",end="")
    print()

