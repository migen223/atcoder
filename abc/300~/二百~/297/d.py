a,b=map(int,input().split())
if a>b:
    big=a
    small=b
else:
    big=b
    small=a

count=0
flag=True
while big!=small:
    if big%small==0:
        print(count+(big//small-1))
        flag=False
        break
    else:
        c=big//small
        count+=c
        big,small=small,big-small*c
        """
        print(big,small)
        if count==30:
            break
        """
        
if flag:
    print(0)