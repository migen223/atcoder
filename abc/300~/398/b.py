a=list(map(int,input().split()))
number=[0]*13
for i in a:
    number[i-1]+=1
three=0
two=0
for i in number:
    if i==2:
        two+=1
    elif i>2:
        three+=1
if two*three!=0 or three>=2:
    print("Yes")
else:
    print("No")
