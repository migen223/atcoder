s=input()
t=input()
check=[]
fill=0
for i in range(1,len(s)):
    if s[i].isupper():
        check.append(s[i-1])
for i in range(len(check)):
    if check[i] in t:
        fill+=1
if fill==len(check):
    print("Yes")
else:
    print("No")
