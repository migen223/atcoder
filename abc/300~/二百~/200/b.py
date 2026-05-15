
n,k=map(int,input().split())


for i in range(k):
    if n%200==0:
        n=n//200
    else:
        s=str(n)
        n=int(s+"200")
print(n)