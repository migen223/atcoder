import sys
a,b,c,d=map(int,input().split())

p=set([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199])

count=0
for i in range(a,b+1):
    for j in range(c,d+1):
        if i+j in p:
            count+=1
            break
if count==(b-a+1):
    print("Aoki")
else:
    print("Takahashi")

