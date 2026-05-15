import sys
b=int(input())

for i in range(1,100):
    if i**i==b:
        print(i)
        sys.exit()
print(-1)