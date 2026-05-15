import math
n=int(input())
ans=[["?"]*n for i in range(n)]
for i in range(math.ceil(n/2)):
    #print(i)
    for j in range(i,n-i):
        
        if i%2==0:
            if j==i or j==n-i-1:
                for k in range(i,n-i):
                    ans[j][k]="#"
            else:
                ans[j][i]="#"
                ans[j][n-i-1]="#"
                
        else:
            if j==i or j==n-i-1:
                #print(i,n-i)
                for k in range(i,n-i):
                    ans[j][k]="."
                    
            else:
                ans[j][i]="."
                ans[j][n-i-1]="."
for i in range(n):
    print("".join(ans[i]))