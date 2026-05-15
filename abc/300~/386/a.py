a=list(map(int,input().split()))
number=[0]*14
for i in a:
    number[i]+=1
two=0
three=0
for i in range(14):
    if number[i]==3:
        three+=1
    elif number[i]==2:
        two+=1
if two==2 or three==1:
    print("Yes")
else:
    print("No")