from math import pow,sqrt
t=int(input())


for i in range(t):
    n=int(input())
    for j in range(2,int(pow(n,1/3))+1):
        if n%j==0:
            if (n//j)%j==0:
                print(j,n//(j*j))
            else:
                print(int(sqrt(n//j)),j)
            break