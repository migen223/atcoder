import sys
n=input()

for i in range(len(n)):
    if n[0]!=n[i]:
        print("No")
        sys.exit()
print("Yes")