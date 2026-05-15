n=int(input())
i=input()
l=list(map(int,i.split()))
check=1
count=0
max=0
countl=[0]*n
"""
for i in range(n):
    for j in l:
        if i<=j:
            count+=1
    countl[i]=count
    count=0
for i in range(n):
    if countl[i]>=i:
        max=i
""" 
while check<=n:
    for i in l:
        if check<=i:
            count+=1
    if count>=check:
        max=check
    else:
        break
    check+=1
    count=0

print(max)
