
q=int(input())

sound=0
mode=0
for i in range(q):
    a=int(input())
    if a==1:
        sound+=1
    elif a==2:
        sound=max(0,sound-1)
    else:
        mode=(mode+1)%2
    
    if sound>=3 and mode==1:
        print("Yes")
    else:
        print("No")

