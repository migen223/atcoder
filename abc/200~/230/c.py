
n,a,b=map(int,input().split())
p,q,r,s=map(int,input().split())

ans=[["."]*(s-r+1) for i in range(q-p+1)]

for i in range(q-p+1):
    for j in range(s-r+1):
        y=p+i
        x=r+j
        #print(y,x)
        
        k1=y-a
        if k1==x-b:
            
            if max(1-a,1-b)<=k1<=min(n-a,n-b):
                ans[i][j]="#"
                #print(i,j)
                #print(a+k1,b+k1)
                #print("One")
                continue
        elif k1==b-x:
            
            if max(1-a,b-n)<=k1<=min(n-a,b-1):
                ans[i][j]="#"
                #print(i,j)
                #print(a+k1,b-k1)
                #print("tow")
                continue


for i in range(q-p+1):
    print("".join(ans[i]))


