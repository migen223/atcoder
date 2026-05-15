s=input()
lens=len(s)
nimotu=[0]*(lens)
for i in range(lens):
    if s[i]=="#":
        nimotu[i]=1
while max(nimotu)==1:
    f=0
    one=-1
    two=-1
    for i in range(lens):
        if nimotu[i]==1 and f==0:
            one=i
            f+=1
            nimotu[i]=0
        if nimotu[i]==1 and f==1:
            two=i
            nimotu[i]=0
            print(f"{one+1},{two+1}")
            break