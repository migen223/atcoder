alpha=[0]*26
s=input()
for i in range(26):
    if s[i]=="A":
        alpha[0]=i
    elif s[i]=="B":
        alpha[1]=i
    elif s[i]=="C":
        alpha[2]=i
    elif s[i]=="D":
        alpha[3]=i
    elif s[i]=="E":
        alpha[4]=i
    elif s[i]=="F":
        alpha[5]=i
    elif s[i]=="G":
        alpha[6]=i
    elif s[i]=="H":
        alpha[7]=i
    elif s[i]=="I":
        alpha[8]=i
    elif s[i]=="J":
        alpha[9]=i
    elif s[i]=="K":
        alpha[10]=i
    elif s[i]=="L":
        alpha[11]=i
    elif s[i]=="M":
        alpha[12]=i
    elif s[i]=="N":
        alpha[13]=i
    elif s[i]=="O":
        alpha[14]=i
    elif s[i]=="P":
        alpha[15]=i
    elif s[i]=="Q":
        alpha[16]=i
    elif s[i]=="R":
        alpha[17]=i
    elif s[i]=="S":
        alpha[18]=i
    elif s[i]=="T":
        alpha[19]=i
    elif s[i]=="U":
        alpha[20]=i
    elif s[i]=="V":
        alpha[21]=i
    elif s[i]=="W":
        alpha[22]=i
    elif s[i]=="X":
        alpha[23]=i
    elif s[i]=="Y":
        alpha[24]=i
    elif s[i]=="Z":
        alpha[25]=i
ans=0
for i in range(1,26):
    ans+=abs(alpha[i]-alpha[i-1])
print(ans)