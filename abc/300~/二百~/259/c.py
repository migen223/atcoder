import sys
s=input()
t=input()

now=s[0]
rens=[]
rent=[]
l=[s[0]]
for i in range(1,len(s)):
    if now!=s[i]:
        rens.append(l)
        l=[s[i]]
        now=s[i]
    else:
        l.append(s[i])
rens.append(l)
now=t[0]
l=[t[0]]

for i in range(1,len(t)):
    if now!=t[i]:
        rent.append(l)
        l=[t[i]]
        now=t[i]
    else:
        l.append(t[i])
rent.append(l)
#print(rens)
#print(rent)

if len(rens)!=len(rent):
    print("No")
else:
    for i in range(len(rens)):
        #print(i)
        if rens[i][0]!=rent[i][0]:
            print("No")
            sys.exit()
        else:
            if len(rens[i])==1 and len(rent[i])>=2:
                print("No")
                sys.exit()
            else:
                if len(rens[i])>len(rent[i]):
                    print("No")
                    sys.exit()
    print("Yes")