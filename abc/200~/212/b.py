x=list(input())
if len(set(x))==1 :
    print("Weak")
else:
    f=0
    for i in range(3):
        if int(x[i+1])==(int(x[i])+1)%10:
            f+=1
    if f==3:
        print("Weak")
    else:
        print("Strong")