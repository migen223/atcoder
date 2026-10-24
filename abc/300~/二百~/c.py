
n=int(input())
two=format(n,'b')
tl=[]
for i in two:
    tl.append(int(i))
#print(tl) 
if n<=120:
    for i in range(n):
        print("A",end="")
else:
    print("AA",end="")
    now=2
    for i in range(1,len(tl)-1):
        if tl[i]==1:
            now+=1
            print("A",end="")
            now*=2
            print("B",end="")
        else:
            print("B",end="")
            now*=2
    if tl[len(tl)-1]==1:
        print("A")