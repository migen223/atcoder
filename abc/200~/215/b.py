from math import pow
n=int(input())
k=0
while (pow(2,k)<=n):
    k+=1
print(k-1)