import sys
n,m=map(int,input().split())


feature=[]
price=[]
for i in range(n):
    se=set()
    l=list(map(int,input().split()))
    price.append(l[0])
    for j in l[2:]:
        se.add(j)
    feature.append(se)

for i in range(n-1):
    for j in range(i+1,n):
        if price[i]<price[j]:
            if feature[i]>=feature[j]:
                print("Yes")
                sys.exit()
        elif price[i]>price[j]:
            if feature[i]<=feature[j]:
                print("Yes")
                sys.exit()
        else:
            if feature[i]>feature[j] or feature[i]<feature[j]:
                print("Yes")
                sys.exit()

print("No")

