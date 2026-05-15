
t=int(input())
for _ in range(t):
    n,d=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    top=0
    now=0
    for i in range(n):
        if a[top]>=b[i]:
            a[top]-=b[i]
            b[i]=0
        elif a[top]==b[i]:
            a[top]=0
            b[i]=0
            top+=1
        else:
            while b[i]>0:
                if a[top]>=b[i]:
                    a[top]-=b[i]
                    b[i]=0
                elif a[top]==b[i]:
                    a[top]=0
                    b[i]=0
                    top+=1
                else:
                    
                    b[i]-=a[top]
                    a[top]=0
                    top+=1
        if 0<=i-d<=n:
            a[i-d]=0
        #print("a",a)
        #print("b",b)
    print(sum(a))