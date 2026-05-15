import sys
s=list(input())
n=len(s)
deta=[]

if n%2==1:
    print("No")
else:
    for i in range(n//2):
        if s[2*i]==s[2*i+1] and s[2*i] not in deta:
            #print(s[2*i])
            deta.append(s[2*i])
        else:
            print("No")
            sys.exit()
    print("Yes")