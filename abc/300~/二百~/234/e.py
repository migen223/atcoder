from bisect import bisect_left
x=int(input())
keta=len(str(x))
ansl=[]

if keta>2:
    for i in range(1,10):
        for j in range(-9,10):
            num=[]
            now=i
            for k in range(keta):
                if 0<=now<=9:
                    num.append(str(now))
                    now+=j
            if len(num)==keta:
                ansl.append(int("".join(num)))
    
    print(ansl[bisect_left(ansl,x)])      
else:
    print(x)        

