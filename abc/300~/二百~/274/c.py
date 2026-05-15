n=int(input())
a=list(map(int,input().split()))
ameba=[0]*(2*n+2)

for i in range(1,n+1):
    #print(ameba)
    ameba[2*i]=ameba[a[i-1]]+1
    ameba[2*i+1]=ameba[a[i-1]]+1

for i in range(1,2*n+2):
    print(ameba[i])