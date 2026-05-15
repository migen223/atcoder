import sys
n=int(input())

se=set(range(1,2*n+2))

while True:
    for i in se:
        pri=i
    print(pri)
    se.remove(pri)
    num=int(input())
    if num==0:
        sys.exit()
    
    
    else:
        se.remove(num)




