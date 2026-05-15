
n=int(input())
count=0

k=len(str(n))
l=[999000,2*999000000,3*999000000000,4*999000000000000]
if k<4:
    print(0)
elif 4<=k<=6:
    print(n-10**3+1)
elif 7<=k<=9:
    print(l[0]+2*(n-10**6+1))
elif 10<=k<=12:
    print(l[0]+l[1]+3*(n-10**9+1))
elif 13<=k<=15:
    print(l[0]+l[1]+l[2]+4*(n-10**12+1))
else:
    print(sum(l)+5)


