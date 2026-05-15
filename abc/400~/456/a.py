import sys
x=int(input())
for i in range(1,7):
    for j in range(1,7):
        for k in range(1,7):
            if i+j+k==x:
                print("Yes")
                sys.exit()

print("No")