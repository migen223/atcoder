import sys
n=input()
for i in range(len(n)-1):
    if n[i]<=n[i+1]:
        print("No")
        sys.exit()
print("Yes")