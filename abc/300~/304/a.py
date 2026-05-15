n=int(input())

age=[]
name=[]
for i in range(n):
    s,a=input().split()
    age.append(int(a))
    name.append(s)
mi=[-1,10**11]
for i in range(n):
    if mi[1]>age[i]:
        mi[1]=age[i]
        mi[0]=i
for i in range(n):
    print(name[(mi[0]+i)%n])


