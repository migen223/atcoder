n=int(input())
count=1
l=[]
l.append(n)
while True:
    if n%2==0:
        n=n//2
    else:
        n=3*n+1
    if n in l:
        print(count+1)
        break
    l.append(n)
    #print(l)
    count+=1
