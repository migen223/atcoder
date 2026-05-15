import sys
s=list(map(int,input().split()))

for i in range(7):
    if s[i]>s[i+1]:
        print("No")
        sys.exit()
for i in range(8):
    if not (100<=s[i]<=675):
        print("No")
        sys.exit()
    if s[i]%25!=0:
        print("No")
        sys.exit()
print("Yes")

