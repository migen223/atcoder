import sys
n,t=map(int,input().split())
a=list(map(int,input().split()))
grid=[[] for i in range(n)]
"""
for i in range(n):
    for j in range(n):
        grid[i].append(n*i+j+1)
        """
tate=[n]*n
yoko=[n]*n
naname=[n]*2
"""
for i in range(n):
    line=set()
    row=set()
    for j in range(n):
        line.add(n*i+j+1)
        row.add(i+n*j+1)
    yoko.append(line)
    tate.append(row)
print(tate)
print(yoko)
"""
nanames=[]
ne1=set()
ne2=set()
for i in range(n):
    ne1.add((n+1)*i+1)
    ne2.add(n+i*(n-1))
nanames.append(ne1)
nanames.append(ne2)
#print(naname)
count=0

for i in range(t):
    count+=1  
    if a[i]%n==0:
        yoko[a[i]//n-1]-=1
        tate[n-1]-=1
        if a[i]//n==n:
            naname[0]-=1
        if a[i]//n==1:
            naname[1]-=1
        if yoko[a[i]//n-1]*tate[n-1]*naname[0]*naname[1]==0:
            print(count)
            sys.exit()
    else:
        yoko[a[i]//n]-=1
        tate[a[i]%n-1]-=1
        if a[i] in nanames[0]:
            naname[0]-=1
        if a[i] in nanames[1]:
            naname[1]-=1
        if yoko[a[i]//n]*tate[a[i]%n-1]*naname[0]*naname[1]==0:
            print(count)
            sys.exit()
    #print(tate)
    #print(yoko)
    #print(naname)

print(-1)
