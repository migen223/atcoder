import sys
n,m=map(int,input().split())
s=[]
t=[]
for i in range(n):
    s.append(list(input()))
for i in range(m):
    t.append(list(input()))


for a in range(n-m+1):
    for b in range(n-m+1):
        count=0
        for i in range(m):
            for j in range(m):
                #print(a,b,i,j)
                if s[a+i][b+j]==t[i][j]:
                    count+=1
                    #print(count)
        if count == m*m:
            print(f"{a+1} {b+1}")
            sys.exit()

