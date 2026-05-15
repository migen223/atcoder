import sys
x,y,z=map(int,input().split())

for i in range(10**7):
    if x+i==(y+i)*z:
        print("Yes")
        sys.exit()

print("No")

    