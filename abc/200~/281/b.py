import sys
s=input()

se=[]
for i in range(65,91):
    se.append(chr(i))

if len(s)==8:
    count=0
    if s[0] not in se:
        print("No")
        sys.exit()
    if s[-1] not in se:
        print("No")
        sys.exit()
    f=0
    for i in range(1,len(s)-1):
        if s[i] in se:
            print("No")
            sys.exit()
        if f==0 and s[i]=="0" :
            print("No")
            sys.exit()
        if f==0 and s[i]!="0":
            f+=1
    print("Yes")
        

else:
    print("No")
