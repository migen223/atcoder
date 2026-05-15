
t=int(input())

for i in range(t):
    a=input()
    b=input()
    ad=[]
    bd=[]
    f=0
    for i in range(len(a)):
        if f==0:
            if a[i]=="x":
                if len(ad)>=1:
                    if ad[-1]==a[i]:
                        f=1
                        ad.pop()
                    else:
                        ad.append(a[i])
                else:
                    ad.append(a[i])
            else:
                ad.append(a[i])
        else:
            if a[i]==")":
                if len(ad)>=1:
                    if ad[-1]=="(":
                        ad.pop()
                    else:
                        f=0
                        ad.append("x")
                        ad.append("x")
                        ad.append(a[i])
                else:
                    f=0
                    ad.append("x")
                    ad.append("x")
                    ad.append(a[i])
            else:
                f=0
                ad.append("x")
                ad.append("x")
                ad.append(a[i])
    if f==1:
        ad.append("x")
        ad.append("x")
    #print()
    #print("ad=","".join(ad),"a=",a)
    f=0
    for i in range(len(b)):
        if f==0:
            if b[i]=="x":
                if len(bd)>=1:
                    if bd[-1]==b[i]:
                        f=1
                        bd.pop()
                    else:
                        bd.append(b[i])
                else:
                    bd.append(b[i])
            else:
                bd.append(b[i])
        else:
            if b[i]==")":
                if len(bd)>=1:
                    if bd[-1]=="(":
                        bd.pop()
                    else:
                        f=0
                        bd.append("x")
                        bd.append("x")
                        bd.append(b[i])
                else:
                    f=0
                    bd.append("x")
                    bd.append("x")
                    bd.append(b[i])
            else:
                f=0
                bd.append("x")
                bd.append("x")
                bd.append(b[i])
    if f==1:
        bd.append("x")
        bd.append("x")
    #print("bd=","".join(bd),"b=",b)
    #print()
    if ad==bd:
        print("Yes")
    else:
        print("No")

