import sys
l=["H","D","S","C"]
l2=["A","2","3","4","5","6","7","8","9","T","J","Q","K"]
se=set()

n=int(input())
s=[]
for i in range(n):
    s.append(input())

for i in range(n):
    if s[i][0] not in l  :
        print("No")
        sys.exit()
    if s[i][1] not in l2:
        print("No")
        sys.exit()
    if s[i] in se:
        print("No")
        sys.exit()
    else:
        se.add(s[i])
print("Yes")  