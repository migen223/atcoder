x,y=map(int,input().split())
count=0
ddouble=0
for i in range(1,7):
    for j in range(1,7):
        if i+j>=x:
            count+=1
            #print(f"{i} {j} i+j>=x")
        if abs(i-j)>=y:
            count+=1
            #print(f"{i} {j} i-j<=x")
        if i+j>=x and abs(i-j)>=y:
            count-=1
            #print(f"{i} {j} 重複")

print(count/36)
        