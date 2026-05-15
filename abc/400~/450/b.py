import sys
n=int(input())

sta=[]
for i in range(n-1):
    c=list(map(int,input().split()))
    sta.append(c)

for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            #print(i,j,k)
            #print(sta[i][j-i-1]+sta[j][k-j-1],sta[i][k-i-1])
            if sta[i][j-i-1]+sta[j][k-j-1]<sta[i][k-i-1]:
                print("Yes")
                sys.exit()

print("No")