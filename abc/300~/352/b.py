s=input()
t=input()
count=0
for i in range(len(t)):
    if count==len(s):
        break
    if t[i]==s[count]:
        count+=1
        print(i+1,end=" ")
print()

