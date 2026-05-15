import sys
s=input()

if s[0]=="1":
    print("No")
else:
    line=[1]*7
    if s[6]=="0":
        line[0]=0
    if s[3]=="0":
        line[1]=0
    if s[7]==s[1]=="0":
        line[2]=0
    if s[4]=="0":
        line[3]=0
    if s[8]==s[2]=="0":
        line[4]=0
    if s[5]=="0":
        line[5]=0
    if s[9]=="0":
        line[6]=0
    #print(line)
    f=0
    for i in range(7):
        #print(f)
        if line[i]==1 and f==0:
            f+=1
            continue
        if line[i]==0 and f==1:
            f+=1
            continue
        if f==2 and line[i]==1:
            print("Yes")
            sys.exit()
    print("No")
    
