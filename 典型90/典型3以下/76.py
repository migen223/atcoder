n=int(input())
a=list(map(int,input().split()))
s=sum(a)
j=s//10
l=0
r=0
su=a[0]
for i in range(n-1):
    a.append(a[i])
if s%10!=0:
    print("No")
elif n==1:
    print("No")
else:
    while l<2*n-1:
        if su<j:
            r+=1
            if r==2*n-1:
                print("No")
                break
            else:
                su+=a[r]
        elif  su>j:
            su-=a[l]
            l+=1
            
        else:
            print("Yes")
            break