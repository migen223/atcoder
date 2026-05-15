m=int(input())
a=[0]*11

for i in range(10,-1,-1):
    a[i]=m//3**i
    m=m%3**i


print(sum(a))
for i in range(11):
    for j in range(a[i]):
        print(i,end=" ")

print()
