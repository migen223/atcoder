
t=int(input())

for _ in range(t):
    n=int(input())
    s=input()
    rle=[]
    now=[s[0],1]
    first=s[0]
    for i in range(1,n):
        if now[0]!=s[i]:
            rle.append(now[1])
            now=[s[i],1]
        else:
            now[1]+=1
    rle.append(now[1])
    max0=0
    max1=0
    ind0=-1
    ind1=-1
    for i in range(0,len(rle),2):
        if rle[i]>max0:
            max0=rle[i]
            ind0=i
        
    for i in range(1,len(rle),2):
        if rle[i]>max1:
            max1=rle[i]
            ind1=i
    #print(rle)
    ans0=0
    ans1=0
    for i in range(len(rle)):
        if ind0!=i:
            if first=="0":
                if i%2==0:
                    ans0+=2*rle[i]
                else:
                    ans0+=rle[i]
            else:
                if i%2==1:
                    ans0+=rle[i]
                else:
                    ans0+=2*rle[i]
        if ind1!=i:
            if first=="0":
                if i%2==0:
                    ans1+=rle[i]
                else:
                    ans1+=2*rle[i]
            else:
                if i%2==1:
                    ans1+=2*rle[i]
                else:
                    ans1+=rle[i]
        #print(ans0,ans1)
    print(min(ans1,ans0))
            

    