
n,x,y=map(int,input().split())
a=list(map(int,input().split()))

even=[]
odd=[]
for i in range(n):
    if i%2==0:
        even.append(a[i])
    else:
        odd.append(a[i])


dpx=[[0]*(2*10*len(even)+1) for i in range(len(even))]
dpy=[[0]*(2*10*len(odd)+1) for i in range(len(odd))]
dpx[0][a[0]]=1
for i in range(1,len(even)):
    for j in range(10*len(even)+1):
        if dpx[i-1][j]==1:
            #print(j,even[i])
            dpx[i][j+even[i]]=1
            dpx[i][j-even[i]]=1
    for j in range(1,10*len(even)+1):
        if dpx[i-1][-j]==1:
            dpx[i][-j-even[i]]=1
            dpx[i][-j+even[i]]=1
dpy[0][odd[0]]=1
dpy[0][-odd[0]]=1
for i in range(1,len(odd)):
    for j in range(10*len(odd)+1):
        
        if dpy[i-1][j]==1:
            #print(i,j,odd[i])
            dpy[i][j+odd[i]]=1
            dpy[i][j-odd[i]]=1
    for j in range(1,10*len(odd)+1):
        if dpy[i-1][-j]==1:
            dpy[i][-j-odd[i]]=1
            dpy[i][-j+odd[i]]=1

"""
for i in range(len(dpx)):
    print(*dpx[i])
print()
for i in range(len(dpy)):
    print(*dpy[i])
"""

if abs(x)>sum(even) or abs(y)>sum(odd):
    print("No")
else:
    if dpx[-1][x]*dpy[-1][y]==1:
        print("Yes")
    else:
        print("No")
    





