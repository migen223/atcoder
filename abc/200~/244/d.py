

s=input().split()
t=input().split()
count=0
for i in range(3):
    if s[i]!=t[i]:
        count+=1
if count==0  or count==3:
    print("Yes")
else:
    print("No")

