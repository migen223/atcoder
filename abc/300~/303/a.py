n=int(input())
s=input()
t=input()

count=0
for i in range(n):
    if s[i]==t[i]:
        count+=1
    if s[i]=="l" and t[i]=="1":
        count+=1
    if s[i]=="1" and t[i]=="l":
        count+=1
    if s[i]=="0" and t[i]=="o":
        count+=1
    if s[i]=="o" and t[i]=="0":
        count+=1
if count==n:
    print("Yes")
else:
    print("No")