import sys
se1=set()
se2=set()
for i in range(97, 123):
    se1.add(chr(i))
#A~Zまでのアルファベットをすべて表示
for i in range(65,91):
    se2.add(chr(i))

s=input()
se=set()
b=0
small=0
for i in range(len(s)):
    se.add(s[i])
    if s[i] in se1:
        small+=1
    if s[i] in se2:
        b+=1
if len(se)==len(s) and b*small!=0:
    print("Yes")
else:
    print("No")