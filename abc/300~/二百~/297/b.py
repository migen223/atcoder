import sys
s=input()

b=[]
k=0
r=[]
for i in range(8):
    if s[i]=="B":
        b.append(i)
    if s[i]=="R":
        r.append(i)
    if s[i]=="K":
        k=i
if b[0]%2==b[1]%2:
    print("No")
    sys.exit()
if r[0]<k<r[1]:
    print("Yes")
else:
    print("No")
