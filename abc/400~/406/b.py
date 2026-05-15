n,k=map(int,input().split())
i=input()
l=list(map(int,i.split()))

number=1
for a in range(n):
    number=number*l[a]
    if number>=10**k:
        number=1
    #print(number)
    
print(number)