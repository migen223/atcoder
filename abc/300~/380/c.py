n,k=map(int,input().split())
s=list(input())
szip=[]

mode=s[0]
number=1
for i in range(1,n):
    if mode==s[i]:
        number+=1
    else:
        szip.append(number)
        mode=s[i]
        number=1
if number!=0:
    szip.append(number)

ans=[]
if n<3:
    print("".join(s))
else:
    if s[0]=="0":
        szip[2*k-1],szip[2*k-2]=szip[2*k-2],szip[2*k-1]
        for i in range(len(szip)):
            if i==2*k-2:
                for j in range(szip[2*k-2]):
                    ans.append("1")
            elif i==2*k-1:
                for j in range(szip[2*k-1]):
                    ans.append("0")
            else:
                if i%2==0:
                    for j in range(szip[i]):
                        ans.append("0")
                else:
                    for j in range(szip[i]):
                        ans.append("1")
            #print(ans)
        print("".join(ans))
    else:
        szip[2*k-2],szip[2*k-3]=szip[2*k-3],szip[2*k-2]
        
        for i in range(len(szip)):
            if i==2*k-3:
                for j in range(szip[2*k-3]):
                    ans.append("1")
            elif i==2*k-2:
                for j in range(szip[2*k-2]):
                    ans.append("0")
            else:
                if i%2==0:
                    for j in range(szip[i]):
                        ans.append("1")
                else:
                    for j in range(szip[i]):
                        ans.append("0")
            #print(ans)
        print("".join(ans)) 


1010011100011001