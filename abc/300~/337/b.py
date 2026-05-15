import sys
s=input()
dic={"A":0,"B":1,"C":2}
number=[]
for i in range(len(s)):
    number.append(dic[s[i]])

for i in range(len(s)-1):
    if number[i]>number[i+1]:
        print("No")
        sys.exit()
print("Yes")

                