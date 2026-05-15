
q=int(input())

now=[]
bra=0
f=0
ind=10**10
for i in range(q):
    que=input().split()
    
    if que[0]=="1":
        c=que[1]
        now.append(c)
        if c=="(":
            bra+=1
        elif c==")":
            bra-=1
        if bra<0:
            f=1
            ind=min(ind,len(now))
    else:
        if f==1 and len(now)==ind:
            f=0
            ind=10**10
        c=now.pop()
        if c=="(":
            bra-=1
        else:
            bra+=1
    #print("".join(now))
    #print(f,bra,ind)
    if f==1:
        print("No")
    else:
        if bra==0:
            print("Yes")
        else:
            print("No")
        

            



