n=input()
x=[]
for i in range(len(n)):
    if n[i]==".":
        break
    else:
        x.append(n[i])
s=int(n[-1])
if 0<=s<=2:
    print("".join(x)+"-")
elif 3<=s<=6:
    print("".join(x))
else:
    print("".join(x)+"+")