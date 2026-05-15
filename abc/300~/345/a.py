from sys import exit
s=input()
if s[0]=="<" and s[-1]==">":
    for i in range(1,len(s)-1):
        if s[i]!="=":
            print("No")
            exit()
    print("Yes")
else:
    print("No")