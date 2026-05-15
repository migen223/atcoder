import sys
n=int(input())
w=input().split()
for i in range(n):
    if w[i] in ["and", "not", "that", "the", "you"]:
        print("Yes")
        sys.exit()
print("No")