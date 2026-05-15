
s=input()
t=input()
correct=0
for i in range(len(t)):
    if s[-len(t)+i]==t[i] or s[-len(t)+i]=="?" or t[i]=="?":
        correct+=1
    
if correct==len(t):
    print("Yes")
else:
    print("No")
for i in range(len(t)):
    if s[-len(t)+i]==t[i] or s[-len(t)+i]=="?" or t[i]=="?":
        correct-=1
    if s[i]==t[i] or s[i]=="?" or t[i]=="?": 
        correct+=1
    if correct==len(t):
        print("Yes")
    else:
        print("No")
    

