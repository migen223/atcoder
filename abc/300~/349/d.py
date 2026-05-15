
l,r=map(int,input().split())


ans=[]
if l%2!=0:
    ans.append((l,l+1))
    l+=1
    while ans[-1][1]!=r:
        k=0
        while l%(2**(k+1))==0:
            k+=1
        #print(l,2**k)
        while l+(2**k)>r:
            k-=1
            #print((2**k),l+(2**k),k)
            if k==-1:
                break
        #print((2**k)*(l//(2**k)))
        #print(F"2^k={2**k}")
        #print(l//(2**k))
        ans.append((l,l+(2**k)))
        #print(ans[-1])
        l+=(2**k)
elif l==0:
    k=0
    while (2**(k+1))<=r:
        k+=1
    l+=2**k
    ans.append((0,2**k))
    while ans[-1][1]!=r:
        k=0
        while l%(2**(k+1))==0:
            k+=1
        #print(l,2**k)
        while l+(2**k)>r:
            k-=1
            #print((2**k),l+(2**k),k)
            if k==-1:
                break
        #print((2**k)*(l//(2**k)))
        #print(F"2^k={2**k}")
        #print(l//(2**k))
        ans.append((l,l+(2**k)))
        #print(ans[-1])
        l+=(2**k)

else:
    k=0
    while l%(2**(k+1))==0:
        k+=1
    #print(l,2**k)
    while l+(2**k)>r:
        k-=1
        #print((2**k),l+(2**k),k)
        if k==-1:
            break
    #print((2**k)*(l//(2**k)))
    #print(F"2^k={2**k}")
    #print(l//(2**k))
    ans.append((l,l+(2**k)))
    #print(ans[-1])
    l+=(2**k)
    while ans[-1][1]!=r:
        k=0
        while l%(2**(k+1))==0:
            k+=1
        #print(l,2**k)
        while l+(2**k)>r:
            k-=1
            #print((2**k),l+(2**k),k)
            if k==-1:
                break
        #print((2**k)*(l//(2**k)))
        #print(F"2^k={2**k}")
        #print(l//(2**k))
        ans.append((l,l+(2**k)))
        #print(ans[-1])
        l+=(2**k)

    
print(len(ans))
for i in ans:
    print(*i)

