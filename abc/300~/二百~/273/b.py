
x,k=map(int,input().split())
x=list(str(x))
if len(x)>=k:
    x.reverse()
    for i in range(k):
        if 0<=int(x[i])<=4:
            x[i]="0"
        else:
            if i+1==len(x):
                x.append("1")
                x[i]="0"
            else:
                count=0
                while i+1+count<len(x):
                    x[i+count]="0"
                    if 10>int(x[i+1+count])+1:
                        x[i+1+count]=str(int(x[i+1+count])+1)
                        break
                    count+=1
                if i+1+count==len(x):
                    x[-1]="0"
                    x.append("1")

        #print(x)
    x.reverse()
    print(int("".join(x)))
else:
    print(0)